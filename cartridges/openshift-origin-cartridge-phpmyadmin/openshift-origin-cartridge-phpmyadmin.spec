%global cartridgedir %{_libexecdir}/openshift/cartridges/v2/phpmyadmin

Summary:       phpMyAdmin support for OpenShift
Name:          openshift-origin-cartridge-phpmyadmin
Version: 1.8.1
Release:       1%{?dist}
Group:         Applications/Internet
License:       ASL 2.0
URL:           https://www.openshift.com
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz
Requires:      rubygem(openshift-origin-node)
Requires:      phpMyAdmin
Requires:      httpd < 2.4
BuildArch:     noarch

%description
Provides phpMyAdmin cartridge support. (Cartridge Format V2)



%prep
%setup -q


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{cartridgedir}
cp -r * %{buildroot}%{cartridgedir}/

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}
%{cartridgedir}/metadata/manifest.yml
%doc %{cartridgedir}/README.md


%changelog
* Thu Apr 25 2013 Adam Miller <admiller@redhat.com> 1.8.1-1
- Split v2 configure into configure/post-configure (ironcladlou@gmail.com)
- more install/post-install scripts (dmcphers@redhat.com)
- Update outdated links in 'cartridges' directory. (asari.ruby@gmail.com)
- Adding V2 Format to all v2 cartridges (calfonso@redhat.com)
- V2 documentation refactoring (ironcladlou@gmail.com)
- bump_minor_versions for sprint 2.0.26 (tdawson@redhat.com)

* Sat Apr 13 2013 Krishna Raman <kraman@gmail.com> 1.7.6-1
- Merge pull request #2065 from jwhonce/wip/manifest_scrub
  (dmcphers+openshiftbot@redhat.com)
- cleanup (dmcphers@redhat.com)
- Bug 951337 (dmcphers@redhat.com)
- WIP Cartridge Refactor - Scrub manifests (jhonce@redhat.com)

* Thu Apr 11 2013 Dan McPherson <dmcphers@redhat.com> 1.7.5-1
- 

* Thu Apr 11 2013 Dan McPherson <dmcphers@redhat.com> 1.7.4-1
- new package built with tito

* Thu Apr 11 2013 Dan McPherson <dmcphers@redhat.com> 1.7.3-1
- new package built with tito

* Wed Apr 10 2013 Adam Miller <admiller@redhat.com> 1.7.2-1
- Delete move/pre-move/post-move hooks, these hooks are no longer needed.
  (rpenta@redhat.com)
