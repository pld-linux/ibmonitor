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
ibmonitor to interaktywna aplikacja terminalowa dla Linuksa pokazuj±ca
zu¿ywane pasmo i ³±czn± ilo¶æ danych przes³anych przez wszystkie
interfejsy.

G³ówne mo¿liwo¶ci to:
- pokazywanie otrzymanego i przes³anego i ca³kowitego pasma ka¿dego
  interfejsu
- obliczanie i wy¶wietlanie ³±czonych warto¶ci wszystkich interfejsów
- wy¶wietlanie ca³kowitej ilo¶ci danych przes³anych przez ka¿dy
  interfejs w KB/MB/GB
- wy¶wietlanie warto¶ci w kilobitach/sekundê (Kbps) i/lub
  kilobajtach/sekundê (KBps)
- pokazywanie maksymalnego pasma zu¿ytego na ka¿dym interfejsie od
  uruchomienia programu
- pokazywanie ¶redniego pasma zu¿ytego na ka¿dym interfejsie od
  uruchomienia programu
- wyj¶cie ze wszystkimi opcjami (maksimum, ¶rednia, wy¶wietlanie w
  Kbps i KBps) z ³atwo¶ci± mieszcz±ce siê na konsoli lub xtermie 80x24
- mo¿liwo¶æ interaktywnej zmiany formatu wy¶wietlania za pomoc±
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
