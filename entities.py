from abc import ABCMeta, abstractmethod, abstractproperty
from datetime import datetime, timedelta
import hash

from exceptions import ValueError, NotImplementedError

from data import Store
from development import DEBUG

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
        
    def __str__(self):
        details = ', '.join(['%s:%s' % (k, self.__dict__[k]) for k in self.Properties])
        return '<%s %s | %s>' % (self.__class__.__name__, self.__dict__[self.Primary], details)

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
        map = {k:self.__dict__[k] for k in self.Properties}
        Store.hmset(key, map)
        return self

class RedisEntity(RedisEntityLoad, RedisEntitySave):
    pass

class UserNameEntry(RedisEntity):
    Primary = 'Name'
    Properties = ['Id',]
    def __init__(self, *args, **kwargs):
        self.Name = kwargs.get('name', None)
        self.Id = kwargs.get('id', None)
    def Validate(self):
        if self.Name is None:
            raise ValueError('Name required, got None')
        if self.Id is None:
            raise ValueError('Id required, got None')
    def GenerateKey(self):
        return 'UserNameEntry:Name:%s' % self.Name

class User(RedisEntity):
    Primary = 'Id'
    Properties = ['Name', 'PasswordHash', 'Secret', 'Created',]
    def __init__(self, *args, **kwargs):
        self.Id = kwargs.get('id', None)
        self.Name = kwargs.get('name', None)
        self.Password = kwargs.get('password', None)
        self.PasswordHash = kwargs.get('password_hash', None)
        self.Secret = kwargs.get('secret', None)
        self.Created = kwargs.get('created', None)
        #print 'secret: %s' % self.Secret.Hex()
        
    def GenerateKey(self):
        return 'User:Id:%s' % self.Id
    def Validate(self):
        if self.Name is None:
            raise ValueError('Name required, got None')
        if self.Password is None:
            raise ValueError('Password required, got None')
        self.PasswordHash = self.DigestPassword()
        if self.Secret is None:
            self.Secret = hash.Secret()
        if self.Created is None:
            self.Created = datetime.utcnow()
        if self.Id is None:
            self.Id = Store.hincrby('User:Info', 'Index')
    def Save(self):
        self.Validate()
        super(User, self).Save();
        UserNameEntry(name=self.Name, id=self.Id).Save()
    
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
        return self.DigestPassword(valid_user.Secret.Value) == valid_user.PasswordHash


# Python will ensure complete implementation by calling __new__
if DEBUG:
    user_test_A = User(name='foo', password='bar', secret=hash.Secret())
    user_test_B = User(name='foo', password='bar', secret=hash.Secret())

    if __name__ == '__main__':
        test = user_test_B.Authenticate(user_test_A)
        if test:
            print 'Access granted.'
        else:
            print 'Access denied.'
    
    bill_nye = User(name='Bill Nye', password='dingledangle')
    bill_nye.Save()
    print bill_nye
    
    bill_nye_lookup = UserNameEntry(name='Bill Nye').Load()
    bill_nye_2 = User(id=bill_nye_lookup.Id).Load()
    print bill_nye_2