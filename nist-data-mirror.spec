Name:           nist-data-mirror
Version:        0.0.1
Release:        1%{?dist}
Summary:        This application is an example for the golang binary RPM spec
License:        ASL 2.0 
Source0:        nist-data-mirror.go
#Source1:        nist-data-mirror.service

BuildRequires:  golang

%description
# include your full description of the application here.

%build
# set up temporary build gopath, and put our directory there
mkdir -p ./_build/src/nist-data-mirror
go get -u github.com/gocolly/colly

export GOPATH=$(pwd)/BUILD:%{gopath}
echo $GOPATH
go build -o nist-data-mirror .

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 ./nist-data-mirror %{buildroot}%{_bindir}/nist-data-mirror

%files
%defattr(-,root,root,-)
%{_bindir}/nist-data-mirror
