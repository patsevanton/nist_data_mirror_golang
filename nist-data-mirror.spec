Name:           nist-data-mirror
Version:        0.1.0
Release:        2%{?dist}
Summary:        A simple Golang command-line utility to mirror the CVE JSON data from NIST.
License:        ASL 2.0 
Source0:        main.go
Source1:        nist-data-mirror.service

BuildRequires:  golang

# Use systemd for fedora >= 18, rhel >=7, SUSE >= 12 SP1 and openSUSE >= 42.1
%define use_systemd (0%{?fedora} && 0%{?fedora} >= 18) || (0%{?rhel} && 0%{?rhel} >= 7) || (!0%{?is_opensuse} && 0%{?suse_version} >=1210) || (0%{?is_opensuse} && 0%{?sle_version} >= 120100)


%description
A simple Golang command-line utility to mirror the CVE XML and JSON data from NIST.

%build
mkdir -p _build/src/github.com/patsevanton/nist_data_mirror_golang
cp ../SOURCES/main.go _build/src/github.com/patsevanton/nist_data_mirror_golang
export GOPATH=$(pwd)/_build
export PATH=$PATH:$(pwd)/_build/bin

go get -u github.com/gocolly/colly
pushd _build/src/github.com/patsevanton/nist_data_mirror_golang
go build -o ../../../../../nist-data-mirror
popd

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}/var/www/repos/nist-data-mirror
install -p -m 0755 ./nist-data-mirror %{buildroot}%{_bindir}/nist-data-mirror

%if %{use_systemd}
%{__mkdir} -p %{buildroot}%{_unitdir}
%{__install} -m644 %{SOURCE1} \
    %{buildroot}%{_unitdir}/%{name}.service
%endif

%post
%if %use_systemd
/usr/bin/systemctl daemon-reload
%endif

%preun
%if %use_systemd
/usr/bin/systemctl stop %{name}
%endif

%postun
%if %use_systemd
/usr/bin/systemctl daemon-reload
%endif

%files
%defattr(-,root,root,-)
%{_bindir}/nist-data-mirror
/var/www/repos/nist-data-mirror
%if %{use_systemd}
%{_unitdir}/%{name}.service
%endif
