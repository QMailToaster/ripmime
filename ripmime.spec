Name:		ripmime
Summary:	ripMIME
Version:	1.4.0.10
Release:	0%{?dist}
License:	BSD
Group:		Networking/Other
URL:		http://www.pldaniels.com/ripmime/
Source0:	http://www.pldaniels.com/ripmime/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
Obsoletes:	ripmime-toaster
BuildRoot:      %{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.%{_arch}

%define debug_package %{nil}

#-------------------------------------------------------------------------------
%description
#-------------------------------------------------------------------------------
ripMIME has a purpose: to extract attached files out of a MIME package.
 
#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------
%setup -q

#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

%{__make}

#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------
rm -rf %{buildroot}

# install directories
#-------------------------------------------------------------------------------
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_datadir}/doc/%{name}-%{version}

# install files
#-------------------------------------------------------------------------------
install $RPM_BUILD_DIR/%{name}-%{version}/ripmime %{buildroot}%{_bindir}
install $RPM_BUILD_DIR/%{name}-%{version}/ripmime.1 %{buildroot}%{_mandir}/man1

# install docs
#-------------------------------------------------------------------------------
for i in CHANGELOG CONTRIBUTORS INSTALL LICENSE README TODO; do
  install $RPM_BUILD_DIR/%{name}-%{version}/$i \
        %{buildroot}%{_datadir}/doc/%{name}-%{version}
done

#-------------------------------------------------------------------------------
%clean 
#-------------------------------------------------------------------------------
rm -rf %{buildroot}

#-------------------------------------------------------------------------------
%files 
#-------------------------------------------------------------------------------
%defattr(-,root,root)
%doc %attr(0644,root,root) %{_datadir}/doc/%{name}-%{version}/*
%attr(0755,root,root) %{_bindir}/ripmime
%attr(0644,root,root) %{_mandir}/man1/*

#-------------------------------------------------------------------------------
%changelog
#-------------------------------------------------------------------------------
* Fri Nov 15 2013 Eric Shubert <eric@datamatters.us> 1.4.0.10-0.qt
- Migrated to github
- Removed -toaster designation
- Added CentOS 6 support
- Removed unsupported cruft
* Fri Jun 12 2009 Jake Vickers <jake@qmailtoaster.com> 1.4.0.6-1.3.6
- Added Fedora 11 support
- Added Fedora 11 x86_64 support
* Thu Jun 11 2009 Jake Vickers <jake@qmailtoaster.com> 1.4.0.6-1.3.6
- Added Mandriva 2009 support
* Thu Apr 23 2009 Jake Vickers <jake@qmailtoaster.com> 1.4.0.6-1.3.5
- Added Fedora 9 x86_64 and Fedora 10 x86_64 support
* Mon Feb 16 2009 Jake Vickers <jake@qmailtoaster.com> 1.4.0.6-1.3.4
- Added Suse 11.1 support
* Mon Feb 09 2009 Jake Vickers <jake@qmailtoaster.com> 1.4.0.6-1.3.4
- Added Fedora 9 and 10 support
* Sat Apr 14 2007 Nick Hemmesch <nick@ndhsoft.com> 1.4.0.6-1.3.3
- Added CentOS 5 i386 support
- Added CentOS 5 x86_64 support
* Wed Nov 01 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 1.4.0.6-1.3.2
- Added Fedora Core 6 support
* Mon Jun 05 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 1.4.0.6-1.3.1
- Initial Package
- Includes SuSE 10.1 support
