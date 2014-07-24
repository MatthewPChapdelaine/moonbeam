
from development import DEBUG

if not DEBUG:
    raise Exception('Cannot run this test in a production environment!')

if __name__ == '__main__':
    user_test_A = User(name='foo', password='bar', secret=hash.Secret())
    user_test_B = User(name='foo', password='bar', secret=hash.Secret())
    test = user_test_B.Authenticate(user_test_A)
    if test:
        print 'Access granted.'
    else:
        print 'Access denied.'

    bill_nye = User(name='Bill Nye', password='dingledangle', email='science.guy@billnye.org')
    bill_nye.Save()
    print bill_nye
    
    bill_nye_lookup = UserNameEntry(name='Bill Nye').Load()
    bill_nye_2 = User(id=bill_nye_lookup.Id).Load()
    print bill_nye_2