Summary:	GNUstep examples
Summary(pl.UTF-8):	Przykłady do GNUstepa
Name:		gnustep-examples
Version:	1.1.0
Release:	2
License:	GPL
Vendor:		The GNUstep Project
Group:		X11/Applications
Source0:	ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz
# Source0-md5:	8ebf37723c89c4fcd4093164ffa50a63
Patch0:		%{name}-pass-arguments.patch
Patch1:		%{name}-install.patch
URL:		http://www.gnustep.org/
BuildRequires:	gnustep-gui-devel >= 0.11.0
Requires:	gnustep-back
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a full collection of examples for the GNUstep libraries. Some
tests are very old, other are newer; some are up-to-date, other are
not.

%description -l pl.UTF-8
To jest pełny zestaw przykładów do bibliotek GNUstep. Część jest
bardzo stara, część nowsza; niektóre są uaktualnione, inne nie.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes

%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes

%{__make} install \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	DESTDIR=$RPM_BUILD_ROOT 

for f in Calculator CurrencyConverter GSTest Ink NSBrowserTest NSImageTest NSPanelTest NSScreenTest md5Digest ; do
	ln -sf %{_libdir}/GNUstep/Applications/$f.app/$f $RPM_BUILD_ROOT/%{_bindir}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README

%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/GNUstep/Applications/*.app
%{_libdir}/GNUstep/Applications/*.app/Resources
%attr(755,root,root) %{_libdir}/GNUstep/Applications/Calculator.app/Calculator
%attr(755,root,root) %{_libdir}/GNUstep/Applications/CurrencyConverter.app/CurrencyConverter
%attr(755,root,root) %{_libdir}/GNUstep/Applications/GSTest.app/GSTest
%attr(755,root,root) %{_libdir}/GNUstep/Applications/Ink.app/Ink
%attr(755,root,root) %{_libdir}/GNUstep/Applications/NSBrowserTest.app/NSBrowserTest
%attr(755,root,root) %{_libdir}/GNUstep/Applications/NSImageTest.app/NSImageTest
%attr(755,root,root) %{_libdir}/GNUstep/Applications/NSPanelTest.app/NSPanelTest
%attr(755,root,root) %{_libdir}/GNUstep/Applications/NSScreenTest.app/NSScreenTest
%attr(755,root,root) %{_libdir}/GNUstep/Applications/md5Digest.app/md5Digest

%dir %{_libdir}/GNUstep/Bundles/*.bundle
%{_libdir}/GNUstep/Bundles/*.bundle/Resources
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/*.bundle/*-test

%dir %{_libdir}/GNUstep/Services/example.service
%{_libdir}/GNUstep/Services/example.service/Resources
%attr(755,root,root) %{_libdir}/GNUstep/Services/example.service/example
