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
ibmonitor is an interactive linux console application which shows
bandwidth consumed and total data transferred on all interfaces.

Its main features are:

    - Shows received, transmitted and total bandwidth of each interface
    - Calculates and displays the combined value of all interfaces
    - Displays total data transferred per interface in KB/MB/GB
    - Values can be displayed in Kbits/sec(Kbps) and/or KBytes/sec(KBps)
    - Can show maximum bandwidth consumed on each interface since start of
      utility
    - Can show average bandwidth consumption on each interface since start
      of utility
    - The output with all features (max, avg and display in Kbps and KBps)
      easily fits on a 80x24 console or xterm
    - Can interactively change its output display format depending on key
      pressed by user.


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
