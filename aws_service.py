import subprocess
import json

class AWSService():
    
    def __init__(self):
        pass
        
    def getS3Usage(self):
        stream = subprocess.run(["sh","cmd.sh"], stdout=subprocess.PIPE)
        data = stream.stdout.decode("utf-8").split('\n')
        respond = {}
        for s3 in data:
            split = s3.split(':')
            if len(split) > 1:
                respond[split[0]] = split[1]
        return respond