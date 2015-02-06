%define debug_package          %{nil}

Name: 	 	caps
Version: 	0.9.7
Release: 	4
Summary: 	Collection of plugins for LADSPA
URL:		http://quitte.de/dsp/
License:	GPLv2+
Group:		Sound
Source0:	http://quitte.de/dsp/caps_0.9.7.tar.bz2
BuildRequires:	ladspa-devel
Requires:	ladspa
Obsoletes:	ladspa-quitte-dsp
Provides:	ladspa-quitte-dsp

%description
CAPS, the C* Audio Plugin Suite, is a collection of refined LADSPA
audio plugins capable of (and mainly intended for) realtime operation.
The suite includes DSP units emulating instrument amplifiers,
stomp-box classics, versatile 'virtual analogue' oscillators, fractal
oscillation, reverb, equalization and more. 

%prep
%setup -q

%build
%make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" DEST=%{_libdir}/ladspa RDFDEST=%{_datadir}/ladspa/rdf
									
%install
%makeinstall DEST=%{buildroot}/%{_libdir}/ladspa RDFDEST=%{buildroot}%{_datadir}/ladspa/rdf

%clean

%files
%doc CHANGES README
%{_libdir}/ladspa/%{name}.so
%{_datadir}/ladspa/rdf/%{name}.rdf

