Name: 	 	caps
Version: 	0.4.2
Release: 	%{mkrel 2}
Summary: 	Collection of plugins for LADSPA
URL:		http://quitte.de/dsp/
License:	GPLv2+
Group:		Sound
Source0:	http://quitte.de/dsp/%{name}_%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{_libdir}/ladspa/%{name}.so
%{_datadir}/ladspa/rdf/%{name}.rdf



%changelog
* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.4.2-2mdv2010.0
+ Revision: 424746
- rebuild

* Thu Aug 28 2008 Adam Williamson <awilliamson@mandriva.org> 0.4.2-1mdv2009.0
+ Revision: 276762
- add fPIC to cflags (needed for build on x86-64)
- provide / obsolete ladspa-quitte-dsp, which it supersedes
- clean (well, completely rewrite) spec
- new release 0.4.2

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.3.0-3mdv2009.0
+ Revision: 243435
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.3.0-1mdv2008.1
+ Revision: 136283
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Pascal Terjan <pterjan@mandriva.org> 0.3.0-1mdv2008.0
+ Revision: 63781
- Import caps



* Sun May 16 2006 Emmanuel Andry <eandry@mandriva.org> 0.3.0-1mdk
- 0.3.0
- drop patch

* Mon Jan 02 2005 Lenny Cartier <lenny@mandriva.com> 0.2.3-1mdk
- 0.2.3
- use debian patch
- add docfiles in docdir

* Wed Jun 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.1.11-2mdk
- Rebuild

* Sat May 8 2004 Austin Acton <austin@mandrake.org> 0.1.11-1mdk
- initial package
