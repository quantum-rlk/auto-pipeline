
import boto3
import uuid
import threading

class S3Mgr:
    def __init__(self,_bucket):
        self.bucket_=_bucket
        self.s3_c=boto3.client('s3')
        self.s3_rc=boto3.resource('s3')

    def push(self,_item):
        l_key=str(uuid.uuid4())
        self.s3_c.upload_file(_item,self.bucket_,l_key)
        return l_key

    def find(self,_key):
        l_res=self.s3_c.get_object(Bucket=self.bucket_,Key=_key)
        return l_res['ContentType']

    def remove(self,_key):
        self.s3_c.delete_object(Bucket=self.bucket_,Key=_key)

    def get(self,_key,_path=""):
        l_path_to_file=__import__('os').getcwd()+'/tmpfile' if _path else _path+'/tmpfile'
        self.s3_rc.meta.client.download_file(self.bucket_,_key,l_path_to_file)
        return __import__('os').getcwd() if _path else _path

    
    def list(self):
        l_res=self.s3_c.list_objects_v2(Bucket=self.bucket_)
        return [ielement['Key'] for ielement in l_res['Contents']] 

    def push_clones(self,_item,_num):
        pool=[]
        for i in range(0,_num):
            pool.append(threading.Thread(target=self.push, args=(_item,),daemon=True))

        for ithread in pool:
            ithread.run()

    def push_bulk(self,*args):
        pool=[]
        for i in args:
            pool.append(threading.Thread(target=self.push, args=(i,),daemon=True))

        for ithread in pool:
            ithread.run()
    
    def flush(self):
        l_res=self.s3_c.list_objects_v2(Bucket=self.bucket_)
        l_list=[ielement['Key'] for ielement in l_res['Contents']]

        pool=[]
        for ielement in l_list:
            pool.append(threading.Thread(target=self.remove, args=(ielement,),daemon=True))

        for ithread in pool:
            ithread.run()

    def count(self):
        return self.s3_c.list_objects_v2(Bucket=self.bucket_)['KeyCount']

#s3=S3Mgr('oblitrium')
#s3.push_clones('network.jpg',20)
#l_key=s3.push('network.jpg')
#l_type=s3.find(l_key)
#print(s3.count())
#s3.remove(l_key)
#print(s3.count())
#l_type=s3.find(l_key)
#print(s3.list())
#s3.flush()
