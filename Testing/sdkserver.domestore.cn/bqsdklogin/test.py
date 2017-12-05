#coding=utf-8
#@作者:yuchunhai
#@Time:17-11-1上午11:15
#@文件名称:test
import rsa
yu = 'iJD84u111111'
pub_key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC52p/pRoZ4SGynOMKWlZjc8DBwMykuyV9r0v7TW/4cnJNXMM5lqe1zNA9nl6rCsSFAcF/3fzXf5UrMFXZXM990RGA3Mr6xIn5NPqc98n2plkH4FQEIQLd7z5Bit6xkJwApAHXToT3FA/KQiuXCB2ma2yCAchEzaEjleuDzqq1ftQIDAQAB'
test1 = rsa.encrypt(b'iJD84u111111',pub_key)
print(test1)