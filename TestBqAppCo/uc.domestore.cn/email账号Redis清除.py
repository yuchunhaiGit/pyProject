# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/29-14:04
#@文件名称:pyProject-email账号Redis清除
import redis
r = redis.StrictRedis(host='192.168.69.229',port=6379,db=0)
# email = 'yuchunhai@qbao.com'
email = 'yuchunhai@domegame.cn'

print(r.hget('uc:basic:email:idx',email))
print(r.hget('uc:db:idx:email',email))
r.hdel('uc:basic:email:idx',email)
r.hdel('uc:db:idx:email',email)

print('---分割线---')
print(r.hget('uc:basic:email:idx',email))
print(r.hget('uc:db:idx:email',email))