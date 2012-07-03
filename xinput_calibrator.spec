Name:           xinput_calibrator
Version:        0.7.5
Release:        %{?dist} 
Summary:        A generic touchscreen calibration program for X.Org

Group:          Applications/System
License:        Creative Commons Attribution-ShareAlike 3.0 License Agreement
URL:            http://www.freedesktop.org/wiki/Software/xinput_calibrator
Source0:        %{name}-%{version}.tbz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      x86_64

%description
A generic touchscreen calibration program for X.Org

%prep
%setup -q -n %{name}-%{version}

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications

install -pm 755 src/xinput_calibrator $RPM_BUILD_ROOT%{_bindir}/xinput_calibrator
install -pm 644 scripts/xinput_calibrator.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/xinput_calibrator.svg
install -pm 644 scripts/xinput_calibrator.desktop $RPM_BUILD_ROOT%{_datadir}/applications/xinput_calibrator.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_bindir}
%{_bindir}/xinput_calibrator

%defattr(-,root,root,-)
%dir %{_datadir}/pixmaps
%{_datadir}/pixmaps/xinput_calibrator.svg

%defattr(-,root,root,-)
%dir %{_datadir}/applications
%{_datadir}/applications/xinput_calibrator.desktop




