from abc import ABCMeta, abstractmethod, abstractproperty
from datetime import datetime, timedelta
from exceptions import Exception, KeyError, ValueError, NotImplementedError

import hash
from data import Store
from permissions import Rule, Directive
from development import DEBUG
from helpers import list_str

class RedisEntityBase:
    __metaclass__ = ABCMeta
    @abstractproperty
    def Primary(self):
        return
    @abstractproperty
    def Properties(self):
        return
    @abstractmethod
    def GenerateKey(self):
        return
    
    def _details_str(self):
        return ', '.join(['%s:%s' % (k, list_str(self.__dict__[k])) for k in self.Properties])
    def _details_repr(self):
        return ', '.join(['%s:%s' % (k, self.__dict__[k]) for k in self.Properties])
    def _repr_format(self, details):
        return '<%s %s | %s>' % (self.__class__.__name__, self.__dict__[self.Primary], details)
    def __str__(self):
        return self._repr_format(self._details_str())
    def __repr__(self):
        return self._repr_format(self._details_repr())

class RedisEntityLoad(RedisEntityBase):
    def Load(self):
        key = self.GenerateKey()
        map = Store.hmget(key, self.Properties)
        for idx, k in enumerate(self.Properties):
            self.__dict__[k] = map[idx]
        return self
        
class RedisEntitySave(RedisEntityBase):
    @abstractmethod
    def Validate(self):
        return
        
    def Save(self):
        key = self.GenerateKey()
        map = {}
        for k in self.Properties:
            v = self.__dict__[k]
            if isinstance(v, RedisEntitySave):
                v.Save()
                map[k] = v.__dict__[v.__class__.Primary]
            else:
                map[k] = v
        Store.hmset(key, map)
        return self

class RedisEntityDelete(RedisEntityBase):
    @abstractmethod
    def Delete(self):
        return
        
class RedisEntityRename(RedisEntityBase):
    @abstractmethod
    def Rename(self):
        return
        
class RedisEntity(RedisEntityLoad, RedisEntitySave):
    pass

class UserNameEntry(RedisEntity, RedisEntityRename):
    Primary = 'Name'
    Properties = ['Id',]
    def __init__(self, *args, **kwargs):
        self.Name = kwargs.get('name', None)
        self.Id = kwargs.get('id', None)
    def GenerateKey(self):
        return 'UserNameEntry:Name:%s' % self.Name
    def Validate(self):
        if self.Name is None:
            raise ValueError('Name required')
        if self.Id is None:
            raise ValueError('Id required')
        find = UserNameEntry(name=self.Name).Load()
        if find.Id is not None and str(self.Id) != str(find.Id):
            raise KeyError('Validation failed: user %s already has name %s' % (find.Id, self.Name))
    def Rename(self, name):
        old = self.GenerateKey()
        try:
            self.Name = name
            print old
            Store.renamenx(old, self.GenerateKey())
            #raise KeyError('Rename failed: existing user with name %s' % (self.Name))
        except Exception as e:
            self.Name = old # Put it back
            raise e
            

class PermissionSet(RedisEntity):
    Primary = 'Id'
    Properties = ['Directives',]
    def __init__(self, *args, **kwargs):
        self.Directives = args
        self.Id = kwargs.get('id', None)
    def GenerateKey(self):
        return 'PermissionSet:Id:%s' % self.Id
    def Validate(self):
        if self.Directives is None:
            raise ValueError('Directives required')
    def Save(self):
        if self.Id is None:
                self.Id = Store.hincrby('PermissionSet:Info', 'Index')
        key = self.GenerateKey()
        Store.sadd(key, self.Directives)
        return self
        
class User(RedisEntity):
    Primary = 'Id'
    Properties = ['Name', 'Email', 'PasswordHash', 'Secret', 'Created', 'PermissionsKey']
    def __init__(self, *args, **kwargs):
        self.Id = kwargs.get('id', None)
        self.Name = kwargs.get('name', None)
        self.Email = kwargs.get('email', None)
        self.Password = kwargs.get('password', None)
        self.PasswordHash = kwargs.get('password_hash', None)
        self.Permissions = kwargs.get('permissions', None)
        self.PermissionsKey = kwargs.get('permissions', None)
        self.Secret = kwargs.get('secret', None)
        self.Created = kwargs.get('created', None)
        #print 'secret: %s' % self.Secret.Hex()
        
    def GenerateKey(self):
        return 'User:Id:%s' % self.Id
    def Validate(self):
        if self.Name is None:
            raise ValueError('Name required')
        if self.Email is None:
            raise ValueError('Email required')
        if self.Password is None:
            if not self.PasswordHash:
                raise ValueError('Password required')
        else:
            self.PasswordHash = self.DigestPassword()
        if self.Secret is None:
            self.Secret = hash.Secret()
        if self.Created is None:
            self.Created = datetime.utcnow()
        if self.Permissions is None:
            self.Permissions = PermissionSet()
        self.Permissions.Validate()

    def Save(self):
        self.Validate()
        if self.Id is None:
            # Hack: skip id check; perform a late update
            entry = UserNameEntry(name=self.Name, id=0)
            entry.Validate()
            entry.Id = self.Id = Store.hincrby('User:Info', 'Index')
            entry.Save()
        else:
            entry = UserNameEntry(name=self.Name, id=self.Id)
            entry.Validate()
            entry.Save()
            old_name = Store.hget(self.GenerateKey(), 'Name')
            if entry.Name != old_name:
                UserNameEntry(name=old_name).Rename(entry.Name)
        self.Permissions.Save()
        super(User, self).Save();
        Store.sadd('User:Entities', self.Id)
    
    def DigestPassword(self, salt = None):
        salt = salt if salt else self.Secret
        return hash.Digest(self.Password, salt)
    def IsRegistered(self):
        return True
    def Authenticate(self, valid_user):
        '''
        self.Secret never used here
        because the user is already
        registered and it is on-file.
        '''
        if DEBUG:
            assert valid_user.IsRegistered()
        return self.DigestPassword(valid_user.Secret) == valid_user.PasswordHash