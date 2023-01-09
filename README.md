# k8s-Questions
Kubwenetes Questions

Q1. Create a Namespace and Deploy deployment of WordPress application and StatefulSet of MySQL in that 
namespace and also create secret in that namespace for store MySQL password and use that secret in WordPress
deployment and MySQL StatefulSets:
  1. Namespace -> wordpress
  2. Deployment name for
      a. WordPress -> wordpress
   Stateful Set name for
      a. MySQL -> mysql
  3. Use images:
      a. Wordpress -> wordpress:4.8-apache
      b. MySQL -> mysql:5.6
  4. Service name:
      a. For Mysql -> mysql
      b. For Wordpress -> wordpress
      (Note: choose correct service type)
  5. Secret name for MySQL -> mysql-secret


Q2. Create a deployment for a super mario game. 
    i) deployment name = mario
   ii) service name = mario 
   iii) service Type = NodePort
   iv) port = 8080
   v) image = docker.io/pengbai/docker-supermario


Q3. Create a pod httpd-storage with image= docker.io/httpd with a volume of type emptyDir. Pod httpd-storage uses volume mount with mount path /root


Q4. There is a file Input.csv containing `hostnames` and their `weightage W` in each line with comma separated values.
hostname format 
``` prefix + $sequence_number + "-" + cluter_id + "." + $region + "." + $environment + "." + domain ```` 

example:
    host30-1001.use1.staging.internal.example.com,1 
    host23-1001.use1.staging.internal.example.com,4

Print count of hostnames for each region & environment. 

Example output: 

Region, Environment, Count 
use1,staging,7 
use1,qa,3 
use1,uat,5 
use1,prod,15 
use2,staging,5 
use2,qa,2 
use2,uat,2 
use2,prod,11 
euc1,staging,4 
euc1,qa,4 
euc1,uat,2 
euc1,prod,10


Q5. Create ansible playbook to install Apache web server independent to OS distribution. (Ubuntu/Centos
