# concourse-test

反映の例
```
// シングルジョブの反映
$ fly -t tutorial set-pipeline -p hello-world -c single/hello-world.yml -l vars/vars.yml -n > /dev/null
// pipelineの反映
$ fly -t tutorial set-pipeline -p sample-pipeline -c pipelines/sample-pipeline.yml -l vars/vars.yml -n > /dev/null
// taskを再実行する場合(環境変数を上書きする)
$ fly -t tutorial execute -c tasks/echo-vars.yml -l vars/vars.yml -v sample-var-01="testtest"
```