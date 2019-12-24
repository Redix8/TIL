# Azure CLI, Cloud shell, PowerShell



## Azure CLI

Command Line Interface 에서 Azure 명령어들을 사용 가능하게한다.

windows, linux 등에서 설치 후 사용 가능하다.



### 1. Azure 로그인

```Azure CLI
az login
```

명령어를 실행하면 브라우저에서 계정 자격 증명으로 로그인한다.

### 2. CLI 사용

로그인 후에는 여러 가지 명령어들로 Azure 서비스를 사용 할 수 있다.

예를 들어,

- 리소스 그룹을 생성

```bash
az group create --name myResourceGroup --location eastus
```

- Windows 2016 datacenter 가 설치된 VM 생성

```bash
az vm create \
    --resource-group myResourceGroup \
    --name myVM \
    --image win2016datacenter \
    --admin-username azureuser \
    --admin-password myPassword
```

- 생성이 완료된다면 다음과 같은 Json 형식이 출력된다.

```json
{
  "fqdns": "",
  "id": "/subscriptions/<guid>/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM",
  "location": "eastus",
  "macAddress": "00-0D-3A-23-9A-49",
  "powerState": "VM running",
  "privateIpAddress": "10.0.0.4",
  "publicIpAddress": "52.174.34.95",
  "resourceGroup": "myResourceGroup"
}
```

## Power Shell

PowerShell은 .NET에서 구축된 작업 기반 명령줄 셸 및 스크립팅 언어입니다. PowerShell을 통해 시스템 관리자 및 고급 사용자는 운영 체제(Linux, macOS 및 Windows) 및 프로세스를 관리하는 작업을 신속하게 자동화할 수 있습니다.

PowerShell 명령을 사용하면 명령줄에서 컴퓨터를 관리할 수 있습니다. PowerShell 공급자는 파일 시스템에 액세스하는 것처럼 쉽게, 레지스트리 및 인증서 저장소와 같은 데이터 저장소에 액세스하도록 지원합니다. PowerShell은 충분한 식을 포함하는 파서와 완전히 개발된 스크립트 언어를 포함합니다.

[MS docs, PowerShell](https://docs.microsoft.com/ko-kr/powershell/scripting/overview?view=powershell-6)

### 0. PowerShell ISE

Powershell 명령어 스크립트화 도구.



### 1. Az Module 설치

```powershell
Install-Module -Name Az -AllowClobber  #Az 모듈 설치
```

```powershell
Set-ExecutionPolicy Unrestricted  #실행 정책을 unrestricted로 
# Restricted : 제한됨
# Unrestricted : 제한되지 않음
```

```powershell
import-module Az.Accounts # 설치한 Az 모듈을 등록
```



### 2. Az Module사용

```powershell
Connect-AzAccount      #account login
Get-AzSubscription     #subscription 확인
Select-AzSubscription -Subscription <Subscription ID> #subscription 선택
```



## Cloud Shell

Azure 에 있는 Cloud Shell로 사용하기 위해서 스토리지 계정을 생성해야된다.

생성 후 Potal 에서 Cloud Shell 을 이용 할 수 있으며, PowerShell 과 Bash중 하나를 선택하여 사용 할 수 있다.







