# VLANs

## Definições
**Oferecem segmentação e flexibilidade organizacional.** Em um grupo de dispositivos em uma VLAN, os elementos comunicam-se como se estivessem conectados ao mesmo cabo, sendo assim, as VLANs são baseadas em conexões lógicas em vez de conexões físicas.

**Permite conectar dispositivos numa rede LAN, mesmo distantes geograficamente.**

As VLANs permitem que o administrador segmente redes com base em fatores como *função, equipe de projeto ou aplicação.* Qualquer porta de um switch pode pertencer a uma VLAN (e apenas umas).

### Benefícios das VLANs:
- *Domínio de transmissões menores*: Dividir uma rede em VLANs reduz o número de dispositivos no domínio de transmissão.
- *Mais segurança:* Somente usuários na mesma VLAN podem se comunicar.
- Maior eficiência de TI: As VLANS simplificam o gerenciamento de rede porque os usuários com rede semelhante podem ser configurados na mesma VLAN.
- *Custo reduzido*: As VLANs reduzem a necessidade de atualizações de rede dispendiosas e usam a largura de banda em uplinks existentes de forma mais eficiente, resultando em redução de custos.
- *Melhor desempenho*: Domínios de difusão menores reduzem o tráfego desnecessário na rede e aumentam o desempenho.
- *Projeto e gerenciamento de aplicativos mais simples*: As VLANs agregam usuários e dispositivos de rede para oferecer suporte a negócios ou requisitos geográficos.

### Tipos de VLANs
- *VLAN padrão:* VLAN configurada inicialmente em um switch (geralmente a VLAN 1). Todas as portas pertencem a ela até que outra VLAN seja configurada.
- *Data VLAN:* Usada para transportar dados dos usuários finais, como tráfego de computadores, notebooks e servidores.
- *VLAN nativa:* VLAN responsável por transportar tráfego **sem tag** em links **tronco** (IEEE 802.1Q). Por padrão, também costuma ser a VLAN 1.
- *VLAN de gerência:* Utilizada para acesso administrativo ao switch (via SSH, Telnet, SNMP, etc.), permitindo gerenciamento remoto do equipamento.
- *VLAN de voz:* VLAN específica para tráfego de voz (VoIP). Prioriza pacotes de áudio para garantir melhor qualidade de chamadas, geralmente com QoS.

`vlan br` lista as VLANs e os dispositivos das redes.

## VLANs em um ambiente de vários switches

Os troncos permitem conectar dispositivos em uma mesma VLAN que estão em diferentes switches. É um link entre dois dispositivos de rede. 

## Algumas perguntas para o chatgpt
### Qual a diferença entre usar uma VLAN ou só segmentar a rede em subredes?

A ideia-chave é: subrede é lógica (camada 3) VLAN é lógica + física (camada 2)

Sub-redes (sem VLAN)
- Funcionam na **Camada 3 (Rede – IP)**
- Você divide a rede usando **endereçamento IP** (ex: `192.168.1.0/24`, `192.168.2.0/24`)
- **Todos os dispositivos continuam no mesmo domínio de broadcast**, se estiverem no mesmo switch
- A separação depende de **roteador** para comunicação entre sub-redes
👉 Problema:  
Mesmo com IPs diferentes, **broadcast continua espalhando** se não houver VLAN.

VLAN (Virtual LAN)
- Funcionam na **Camada 2 (Enlace)**    
- Criam **redes logicamente separadas** dentro do mesmo switch
- Cada VLAN é um **domínio de broadcast separado**
- Pode usar **o mesmo switch físico** para várias redes isoladas
👉 Vantagem:  
Reduz broadcast, melhora desempenho e aumenta segurança.
