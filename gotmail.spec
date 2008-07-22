%define name	gotmail
%define version	0.9.0
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	Fetches mail from a Hotmail or MSN webmail account
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Patch0:		gotmail-0.90.patch
URL:		http://gotmail.sourceforge.net/
License:	GPL
Group:		Networking/Mail
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	curl
BuildArch:	noarch

%description
This is Gotmail, a perl script to fetch mail out of your Hotmail
or MSN account. This is especially useful if you want to move from
Hotmail into one of the other free mail services - one command can
do it all. Gotmail also supports getting any new mail only from your
Hotmail or MSN account - perfect for using a Hotmail account as a
redirect address into another account.

Also included is a script for use with Evolution.

%prep
%setup -q

%patch0 -p1 -b .gotmail

%build
%make
										
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="%{buildroot}" BINDIR=%{_bindir} MANDIR=%{_mandir}
#install -o root -g root -m 755 gotmail4evolution %buildroot/%_bindir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README sample.gotmailrc 
%{_bindir}/*
%{_mandir}/man1/*
