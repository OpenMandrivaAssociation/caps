%define name	caps
%define version	0.3.0
%define release	%mkrel 1

Summary:      	The C* Audio Plugin Suite
Name:         	%name
Version:      	%version
Release:      	%release
License:    	GPL
Group:        	Sound
URL:          	http://quitte.de/dsp/caps.html
Source0:      	%{name}-%{version}.tar.bz2
#Patch0:		%name.patch.bz2

%description
caps, the C* Audio Plugin Suite, is a collection of refined LADSPA
units including instrument amplifier emulation, stomp-box classics,
versatile 'virtual analog' oscillators, fractal oscillation, reverb,
equalization and others.

%prep
%setup -q

#%patch0 -p1

%build
make DEST=%{_libdir}/ladspa

%install
rm -rf $RPM_BUILD_ROOT
make DEST=$RPM_BUILD_ROOT%{_libdir}/ladspa install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES COPYING README* HACKING 
%doc caps.html 
%dir %{_libdir}/ladspa
%{_libdir}/ladspa/*.so
