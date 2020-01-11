A simple Golang command-line utility to mirror the CVE JSON data from NIST.

```bash
yum -y install yum-plugin-copr

yum copr enable antonpatsev/nist_data_mirror_golang

yum -y install nist-data-mirror

systemctl start nist-data-mirror
```

nist-data-mirror mirror the CVE JSON data from NIST to /var/www/repos/nist-data-mirror/
