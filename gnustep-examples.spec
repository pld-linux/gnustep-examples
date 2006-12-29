Summary:	GNUstep examples
Summary(pl):	Przyk³ady do GNUstepa
Name:		gnustep-examples
Version:	1.1.0
Release:	1
License:	GPL
Vendor:		The GNUstep Project
Group:		X11/Applications
Source0:	ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz
# Source0-md5:	8ebf37723c89c4fcd4093164ffa50a63
Patch0:		%{name}-pass-arguments.patch
URL:		http://www.gnustep.org/
BuildRequires:	gnustep-gui-devel >= 0.11.0
Requires:	gnustep-back
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%description
This is a full collection of examples for the GNUstep libraries. Some
tests are very old, other are newer; some are up-to-date, other are
not.

%description -l pl
To jest pe³ny zestaw przyk³adów do bibliotek GNUstep. Czê¶æ jest
bardzo stara, czê¶æ nowsza; niektóre s± uaktualnione, inne nie.

%prep
%setup -q
%patch0 -p1

%build
export GNUSTEP_MAKEFILES=%{_prefix}/System/Library/Makefiles
export GNUSTEP_FLATTENED=yes

%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_prefix}/System/Library/Makefiles
export GNUSTEP_FLATTENED=yes

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README

%dir %{_prefix}/System/Applications/*.app
%{_prefix}/System/Applications/*.app/Resources
%{_prefix}/System/Applications/*.app/*.openapp
%attr(755,root,root) %{_prefix}/System/Applications/Calculator.app/Calculator
%attr(755,root,root) %{_prefix}/System/Applications/CurrencyConverter.app/CurrencyConverter
%attr(755,root,root) %{_prefix}/System/Applications/GSTest.app/GSTest
%attr(755,root,root) %{_prefix}/System/Applications/Ink.app/Ink
%attr(755,root,root) %{_prefix}/System/Applications/NSBrowserTest.app/NSBrowserTest
%attr(755,root,root) %{_prefix}/System/Applications/NSImageTest.app/NSImageTest
%attr(755,root,root) %{_prefix}/System/Applications/NSPanelTest.app/NSPanelTest
%attr(755,root,root) %{_prefix}/System/Applications/NSScreenTest.app/NSScreenTest
%attr(755,root,root) %{_prefix}/System/Applications/md5Digest.app/md5Digest

%dir %{_prefix}/System/Library/ApplicationSupport/GSTest
%dir %{_prefix}/System/Library/ApplicationSupport/GSTest/*.bundle
%{_prefix}/System/Library/ApplicationSupport/GSTest/*.bundle/Resources
%attr(755,root,root) %{_prefix}/System/Library/ApplicationSupport/GSTest/*.bundle/[!Rs]*

%dir %{_prefix}/System/Library/Services/example.service
%{_prefix}/System/Library/Services/example.service/Resources
%attr(755,root,root) %{_prefix}/System/Library/Services/example.service/example
