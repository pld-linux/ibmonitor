Summary:	Interactive Bandwidth Monitor
Name:		ibmonitor
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/ibmonitor/%{name}-%{version}.tar.gz
# Source0-md5:	6f37ee0b00b62822823cdbabc9d7419e
URL:		http://ibmonitor.sourceforge.net/
Requires:	perl-Term-ANSIColor
Requires:	perl-Term-ReadKey
Requires:	perl-Time-HiRes
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install ibmonitor $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
