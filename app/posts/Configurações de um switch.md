# Configurações de um switch

---

### Configuração da interface de gerenciamento
```{ bash }
S1# configure terminal
S1(config)# interface vlan 99
S1(config-if)# ip address 172.17.99.11 255.255.255.0
S1(config-if)# ipv6 address 2001:db8:acad:99::1/64
S1(config-if)# no shutdown
S1(config-if)# end
S1# copy running-config startup-config
```


### Configuração do gateway padrão
```
S1# configure terminal
S1(config)# ip default-gateway 172.17.99.1
S1(config-if)# end
S1# copy running-config startup-config
```

### Verificação das configurações

```
S1# show ip interface brief
```

---

### Configuração das portas de switch na camada física (tipo de comunicação)
```
S1# configure terminal
S1(config)# interface FastEthernet 0/1
S1(config-if)# duplex full
S1(config-if)# speed 100
S1(config-if)# end
S1# copy running-config startup-config
```
### MDIX Automático
```
S1(config-if)# mdix auto
```

### Comandos de verificação de switch
```
S1# show intefaces [interface-id]
S1# show startup-config
S1# show runnig-config
S1# show flash
S1# show version
S1# show history
S1# show ip [ou ipv6] interface [interface-id]
S1# show mac-address-table
```

### Configuração de acesso remoto via SSH

```
S1# show ip ssh
S1# configure terminal
S1(config)# ip domain-name cisco.com
S1(config)# crypto key generate rsa
S1(config)# username admin secret password
S1(config)# line vty 0 15
S1(config-line)# transport input ssh
S1(config-line)# login local
S1(config-line)# exit
S1(config)# ip ssh version 2
```
