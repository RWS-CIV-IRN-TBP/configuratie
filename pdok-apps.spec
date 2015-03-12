#!/usr/bin/rpmbuild -ba
# to build for trunk from svn workdir, add -D 'trunk 1'

%define         version 1.0.5

Name:           pdok-apps
Version:        %{version}
Release:        1

%define         install_user     apache
%define         prefix          /apps
%define         apps_prefix %{prefix}/geoservices

Summary:        PDOK applications
License:        GPLv3
Group:          Applications/Internet
Packager:       Milo van der Linden
Source:         pdok-apps-%{version}.tgz

BuildArch:      noarch
Buildroot:      %{_tmppath}/%{name}-root
Prefix:         %{prefix}

Requires:       httpd
Autoreq:        1

%description
pdokkaart javascript module and applications created for Rijkswaterstaat that us the pdokkaart or the pdokkaart-api. Applications can be found in subpackages.

%package -n pdok-apps-vegetatielegger
Summary:        vegetatielegger
Group:          Applications/Internet
Requires:       pdok-apps
%description -n pdok-apps-vegetatielegger
pdokkaart vegetatielegger application.

%package -n pdok-apps-kustlijnkaart
Summary:        kustlijnkaart
Group:          Applications/Internet
Requires:       pdok-apps
%description -n pdok-apps-kustlijnkaart
pdokkaart kustlijnkaart application.

%prep
%setup -q -n pdok-apps-%{version}

%build
# remove unwanted files

# skip brp-strip* at end of install (not needed for noarch)
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
# services
%{__mkdir} -p $RPM_BUILD_ROOT/%{apps_prefix}
%{__cp} -a * $RPM_BUILD_ROOT/%{apps_prefix}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%pre
#nothing
%post -n pdok-apps
/sbin/service httpd reload
#nothing
%post -n pdok-apps-vegetatielegger
#nothing
%post -n pdok-apps-kustlijnkaart


%preun

%postun

%files -n pdok-apps
%defattr(-,%{install_user},%{install_user})
%config(noreplace) %{apps_prefix}/httpd.d/pdok_apps.conf
%dir               %{apps_prefix}/apps/pdokkaart
%exclude           %{apps_prefix}/apps/pdokkaart/.gitignore
%{apps_prefix}/apps/pdokkaart/*

%files -n pdok-apps-vegetatielegger
%defattr(-,%{install_user},%{install_user})
%dir               %{apps_prefix}/apps/vegetatielegger
%exclude           %{apps_prefix}/apps/vegetatielegger/.gitignore
%{apps_prefix}/apps/vegetatielegger/*

%files -n pdok-apps-kustlijnkaart
%defattr(-,%{install_user},%{install_user})
%dir               %{apps_prefix}/apps/kustlijnkaart
%exclude           %{apps_prefix}/apps/kustlijnkaart/.gitignore
%{apps_prefix}/apps/kustlijnkaart/*


%changelog
* Thu Mar 12 2015 Milo van der Linden  1.0.5-1
- Switched to RWS-CIV-IRN-TBP repository
- Kustlijnkaart added
* Wed Mar 11 2015 Richard Duivenvoorde 1.0.4-1
- Switched to geonovum repository
- Various cosmetic fixes
* Mon Jan 13 2015 Raymond Nijssen      1.0.3-4
- Proxy fix
* Mon Jan 13 2015 Raymond Nijssen      1.0.3-3
- Fix for broken OpenLayers in responsive web pages
* Wed Jan  7 2015 Raymond Nijssen      1.0.3-2
* Tue Jan  6 2015 Raymond Nijssen      1.0.3-1
* Mon Jan  5 2015 Richard Duivenvoorde 1.0.2-1
- Fix for vegetatielegger
* Mon Jan  5 2015 Raymond Nijssen      1.0.1-1
- Fix for IE8
* Wed Nov  5 2014 Milo van der Linden  1.0.0-1
- Initial version.
