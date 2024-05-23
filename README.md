How's it work ?

Example usage

```
python3 main.py --template [minimal,complex] \
    --kind [Pod, Deployment, Service] \
    --name [Pod name] \
    --label [label] --labelValue [labelValue] \
    --containerName [containerName \
    --imageName [imageName] \
    --port [port] \
    --output [Specify the output path to save the file]

```

```
python3 main.py --template minimal \
    --kind Pod \
    --name nginx-test \
    --label app --labelValue nginx \
    --containerName nginx-pod \
    --imageName nginx:latest \
    --port 8080 \
    --output /home/user/manifest/nginx.yaml
```
