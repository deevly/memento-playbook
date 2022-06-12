## Encrypt with KMS
```
ansible-playbook -e "target=<RAW_STRING> kms_key=<KMS_KEY>" encrypt.yaml
```

## Deploy Kafka
```
ansible-playbook -i inventories/host -e "kms_key=<KNS_KEY>" install.yaml
```

### Notice
Set `OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES`
```
➜  memento-playbook (master) export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```
