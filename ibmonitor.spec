Summary:	Interactive Bandwidth Monitor
Summary(pl):	Interaktywny monitor wykorzystania pasma
Name:		ibmonitor
Version:	1.3
Release:	1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/ibmonitor/%{name}-%{version}.tar.gz
# Source0-md5:	6f37ee0b00b62822823cdbabc9d7419e
URL:		http://ibmonitor.sourceforge.net/
Requires:	perl-Term-ANSIColor
Requires:	perl-Term-ReadKey
Requires:	perl-Time-HiRes
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ibmonitor is an interactive Linux console application which shows
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

%description -l pl
ibmonitor to interaktywna aplikacja terminalowa dla Linuksa pokazuj�ca
zu�ywane pasmo i ��czn� ilo�� danych przes�anych przez wszystkie
interfejsy.

G��wne mo�liwo�ci to:
- pokazywanie otrzymanego i przes�anego i ca�kowitego pasma ka�dego
  interfejsu
- obliczanie i wy�wietlanie ��czonych warto�ci wszystkich interfejs�w
- wy�wietlanie ca�kowitej ilo�ci danych przes�anych przez ka�dy
  interfejs w KB/MB/GB
- wy�wietlanie warto�ci w kilobitach/sekund� (Kbps) i/lub
  kilobajtach/sekund� (KBps)
- pokazywanie maksymalnego pasma zu�ytego na ka�dym interfejsie od
  uruchomienia programu
- pokazywanie �redniego pasma zu�ytego na ka�dym interfejsie od
  uruchomienia programu
- wyj�cie ze wszystkimi opcjami (maksimum, �rednia, wy�wietlanie w
  Kbps i KBps) z �atwo�ci� mieszcz�ce si� na konsoli lub xtermie 80x24
- mo�liwo�� interaktywnej zmiany formatu wy�wietlania za pomoc�
  klawiszy.

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
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
