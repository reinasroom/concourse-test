# concourse-test

反映の例
```
// シングルジョブの反映
$ fly -t tutorial set-pipeline -p hello-world -c single/hello-world.yml --load-vars-from=vars/vars.yml -n > /dev/null
// pipelineの反映
$ fly -t tutorial set-pipeline -p sample-pipeline -c pipeline/sample-pipeline.yml --load-vars-from=vars/vars.yml -n > /dev/null
```