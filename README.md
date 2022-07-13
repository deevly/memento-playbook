# Memento Playbook
Memento Playbook for Kafka & Zookeeper Cluster.

## Playbooks
### Encrypt Data using KMS Key
```
ansible-playbook -e "target=<RAW_STRING> kms_key=<KMS_KEY>" encrypt.yaml
```

### Deploy Kafka
```
ansible-playbook -i inventories/host -e "kms_key=<KNS_KEY>" install.yaml
```

### Note
Set `OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES` in M1 Mac
```
➜  memento-playbook (master) export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```
