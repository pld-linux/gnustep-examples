Summary:	GNUstep examples
Summary(pl):	Przyk³ady do GNUstepa
Name:		gnustep-examples
Version:	0.9.7
Release:	3
License:	GPL
Vendor:		The GNUstep Project
Group:		X11/Applications
Source0:	ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz
# Source0-md5:	61809c02a84e286a057d16c1648e8942
Patch0:		%{name}-paths.patch
Patch1:		%{name}-pass-arguments.patch
URL:		http://www.gnustep.org/
BuildRequires:	gnustep-gui-devel
Requires:	gnustep-back
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

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
%patch1 -p1

%build
. %{_prefix}/System/Makefiles/GNUstep.sh

%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Makefiles/GNUstep.sh

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
%dir %{_prefix}/System/Applications/*.app/%{gscpu}
%dir %{_prefix}/System/Applications/*.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/*.app/%{gscpu}/%{gsos}/%{libcombo}
%{_prefix}/System/Applications/*.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
%attr(755,root,root) %{_prefix}/System/Applications/Calculator.app/Calculator
%attr(755,root,root) %{_prefix}/System/Applications/Calculator.app/%{gscpu}/%{gsos}/%{libcombo}/Calculator
%attr(755,root,root) %{_prefix}/System/Applications/CurrencyConverter.app/CurrencyConverter
%attr(755,root,root) %{_prefix}/System/Applications/CurrencyConverter.app/%{gscpu}/%{gsos}/%{libcombo}/CurrencyConverter
%attr(755,root,root) %{_prefix}/System/Applications/GSTest.app/GSTest
%attr(755,root,root) %{_prefix}/System/Applications/GSTest.app/%{gscpu}/%{gsos}/%{libcombo}/GSTest
%attr(755,root,root) %{_prefix}/System/Applications/Ink.app/Ink
%attr(755,root,root) %{_prefix}/System/Applications/Ink.app/%{gscpu}/%{gsos}/%{libcombo}/Ink
%attr(755,root,root) %{_prefix}/System/Applications/NSBrowserTest.app/NSBrowserTest
%attr(755,root,root) %{_prefix}/System/Applications/NSBrowserTest.app/%{gscpu}/%{gsos}/%{libcombo}/NSBrowserTest
%attr(755,root,root) %{_prefix}/System/Applications/NSPanelTest.app/NSPanelTest
%attr(755,root,root) %{_prefix}/System/Applications/NSPanelTest.app/%{gscpu}/%{gsos}/%{libcombo}/NSPanelTest
%attr(755,root,root) %{_prefix}/System/Applications/NSScreenTest.app/NSScreenTest
%attr(755,root,root) %{_prefix}/System/Applications/NSScreenTest.app/%{gscpu}/%{gsos}/%{libcombo}/NSScreenTest

%dir %{_prefix}/System/Library/Bundles/*.bundle
%{_prefix}/System/Library/Bundles/*.bundle/Resources
%attr(755,root,root) %{_prefix}/System/Library/Bundles/*.bundle/%{gscpu}
