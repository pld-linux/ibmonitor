Summary:	Interactive Bandwidth Monitor
Summary(pl.UTF-8):	Interaktywny monitor wykorzystania pasma
Name:		ibmonitor
Version:	1.4
Release:	1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/ibmonitor/%{name}-%{version}.tar.gz
# Source0-md5:	b8522eda27381b4e65eed12bffd8adcd
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

%description -l pl.UTF-8
ibmonitor to interaktywna aplikacja terminalowa dla Linuksa pokazująca
zużywane pasmo i łączną ilość danych przesłanych przez wszystkie
interfejsy.

Główne możliwości to:
- pokazywanie otrzymanego i przesłanego i całkowitego pasma każdego
  interfejsu
- obliczanie i wyświetlanie łączonych wartości wszystkich interfejsów
- wyświetlanie całkowitej ilości danych przesłanych przez każdy
  interfejs w KB/MB/GB
- wyświetlanie wartości w kilobitach/sekundę (Kbps) i/lub
  kilobajtach/sekundę (KBps)
- pokazywanie maksymalnego pasma zużytego na każdym interfejsie od
  uruchomienia programu
- pokazywanie średniego pasma zużytego na każdym interfejsie od
  uruchomienia programu
- wyjście ze wszystkimi opcjami (maksimum, średnia, wyświetlanie w
  Kbps i KBps) z łatwością mieszczące się na konsoli lub xtermie 80x24
- możliwość interaktywnej zmiany formatu wyświetlania za pomocą
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
