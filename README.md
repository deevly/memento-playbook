## Encrypt with KMS
```
ansible-playbook -e "target=<RAW_STRING> kms_key=<KMS_KEY>" encrypt.yaml
```

## Deploy Kafka
```
ansible-playbook -i inventories/host -e "kms_key=<KNS_KEY>" install.yaml
```
