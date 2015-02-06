%define name	gotmail
%define version	0.9.0
%define release 7

Name: 	 	%{name}
Summary: 	Fetches mail from a Hotmail or MSN webmail account
Version: 	%{version}
Release: 	%{release}
Source:		%{name}-%{version}.tar.bz2
Patch0:		gotmail-0.90.patch
URL:		http://gotmail.sourceforge.net/
License:	GPLv2
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


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-6mdv2011.0
+ Revision: 610970
- rebuild

* Tue Feb 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.9.0-5mdv2010.1
+ Revision: 502960
- fix licence

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.9.0-4mdv2010.0
+ Revision: 429290
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.9.0-3mdv2009.0
+ Revision: 240794
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 05 2007 Jérôme Soyer <saispo@mandriva.org> 0.9.0-1mdv2008.0
+ Revision: 80070
- Add Patch0
- Import gotmail



* Sat Apr 29 2006 Austin Acton <austin@mandriva.org> 0.8.9-1mdk
- New release 0.8.9

* Mon Mar  6 2006 Austin Acton <austin@mandriva.org> 0.8.8-1mdk
- initial package
