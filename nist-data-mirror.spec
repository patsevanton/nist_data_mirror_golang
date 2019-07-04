Name:           nist-data-mirror
Version:        0.0.5
Release:        1%{?dist}
Summary:        A simple Golang command-line utility to mirror the CVE JSON data from NIST.
License:        ASL 2.0 
Source0:        main.go
Source1:        nist-data-mirror.service

BuildRequires:  golang

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
install -p -m 0755 ./nist-data-mirror %{buildroot}%{_bindir}/nist-data-mirror

%files
%defattr(-,root,root,-)
%{_bindir}/nist-data-mirror
