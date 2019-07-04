Name:           nist-data-mirror
Version:        0.0.1
Release:        1%{?dist}
Summary:        This application is an example for the golang binary RPM spec
License:        ASL 2.0 
Source0:        main.go
#Source1:        nist-data-mirror.service

BuildRequires:  golang

%description
# include your full description of the application here.

%build
#mkdir -p ./_build/src/github.com/patsevanton/
#ln -s $(pwd) ./_build/src/github.com/patsevanton/nist_data_mirror_golang
export GOPATH=$(pwd)/_build
export PATH=$PATH:$(pwd)/_build/bin
echo $GOPATH

go get -u github.com/gocolly/colly
#go get -u github.com/kardianos/govendor
#pushd _build/src/github.com/patsevanton/nist_data_mirror_golang
pwd
#govendor sync
go build 
#popd

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 ./nist-data-mirror %{buildroot}%{_bindir}/nist-data-mirror

%files
%defattr(-,root,root,-)
%{_bindir}/nist-data-mirror
