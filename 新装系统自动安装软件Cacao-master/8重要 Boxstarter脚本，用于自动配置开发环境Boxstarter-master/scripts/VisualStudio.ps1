# Install Visual Studio and workloads
choco install -y visualstudio2019enterprise
choco install -y visualstudio2019-workload-azure
choco install -y visualstudio2019-workload-data
choco install -y visualstudio2019-workload-manageddesktop
choco install -y visualstudio2019-workload-netcoretools
choco install -y visualstudio2019-workload-netweb
choco install -y visualstudio2019-workload-python
choco install -y ssis-vs2019

# Add Barker nuget feed
nuget sources Add -Name "BarkerFeed" -Source https://pkgs.dev.azure.com/BarkerCollegeDev/_packaging/BarkerFeed/nuget/v3/index.json
