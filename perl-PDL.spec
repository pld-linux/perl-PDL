%include	/usr/lib/rpm/macros.perl
%define		__find_provides	%{_builddir}/PDL-%{version}/find-perl-provides
%define		__find_requires %{_builddir}/PDL-%{version}/find-perl-requires
Summary:	perlDL
Summary(pl):	perlDL
Name:		perl-PDL
Version:	2.1.2cvs20001124
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://download.sourceforge.net/pub/sourceforge/PDL/PDL-%{version}.tar.gz
Patch0:		%{name}-conf.patch
Patch1:		%{name}-dep.patch
URL:		http://www.perl.com/CPAN//modules/by-module/PDL/PDL-%{version}.readme
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6.0-2
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	perl-Tk
BuildRequires:	perl-PGPLOT
BuildRequires:	perl-ExtUtils-F77 >= 1.10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The perlDL project aims to turn perl into an efficient numerical
language for scientific computing. The PDL module gives standard perl
the ability to COMPACTLY store and SPEEDILY manipulate the large
N-dimensional data sets which are the bread and butter of scientific
computing. e.g. C<$a=$b+$c> can add two 2048x2048 images in only a
fraction of a second.

%description -l pl
perlDL rozsze¿a mo¿liwo¶ci perl'a o funkcje do obliczeñ numerycznych i
naukowaych.

%package perldl
Summary:	PDL shell
Summary(pl):	Pow³oka PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description perldl

%description -l pl perldl

%package Graphics-TriD
Summary:	PDL 3D interface
Summary(pl):	Interfejs 3D dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description Graphics-TriD

%description -l pl Graphics-TriD

%package Graphics-TriD-Tk
Summary:	A Tk widget interface to the PDL-Graphics-TriD
Summary(pl):	Kontrolka interfejsu Tk dla PDL-Graphics-TriD
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description Graphics-TriD-Tk

%description -l pl Graphics-TriD-Tk

%package Graphics-PGPLOT
Summary:	PGPLOT enhanced interface for PDL
Summary(pl):	Rozszerzony interfejs biblioteki PGPLOT dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description Graphics-PGPLOT

%description -l pl Graphics-PGPLOT

%package Graphics-IIS
Summary:	Display PDL images on IIS devices (saoimage/ximtool)
Summary(pl):	Wy¶wietlanie grafiki PDL na urz±dzeniach IIS (saoimage/ximtool)
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description Graphics-IIS

%description -l pl Graphics-IIS

%package Graphics-LUT
Summary:	Provides access to a number of look-up tables for PDL
Summary(pl):	N/A
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description Graphics-LUT

%description -l pl Graphics-LUT

%package Graphics-OpenGL
Summary:	 PDL interface to the OpenGL graphics library
Summary(pl):	Interfejs OpenGL dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description Graphics-OpenGL

%description -l pl Graphics-OpenGL

%package IO-Browser
Summary:	2D data browser for PDL
Summary(pl):	Przegl±darka danych 2D dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description IO-Browser

%description -l pl IO-Browser

%package IO-FastRaw
Summary:	A simple, fast and convenient IO format for PDL
Summary(pl):	Prosty, szybki i wygodny format wej¶cia/wyj¶cia dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description IO-FastRaw

%description -l pl IO-FastRaw

%package IO-FlexRaw
Summary:	 A flexible binary IO format for PDL
Summary(pl):	Elastyczny binarny format wej¶cia/wyj¶cia dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description IO-FlexRaw

%description -l pl IO-FlexRaw

%package IO-NDF
Summary:	Starlink N-dimensional data structures for PDL
Summary(pl):	Wsparcie dla n-wymiarowych struktur danych firmy Starlink dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description IO-NDF

%description -l pl IO-NDF

%package IO-Pic
Summary:	IO-Pic
Summary(pl):	IO-Pic
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Requires:	netpbm

%description IO-Pic

%description -l pl IO-Pic

%package IO-Pnm
Summary:	PNM format IO for PDL
Summary(pl):	Wsparcie dla formatu PNM dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description IO-Pnm

%description -l pl IO-Pnm

%package Demos
Summary:	PDL demos
Summary(pl):	Przyk³adowe skrypty z u¿yciem PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description Demos

%description -l pl Demos

%prep
%setup  -q -n PDL-%{version}
%patch0 -p1 
%patch1 -p1

chmod +x find-*

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g} -I%{_includedir}/ncurses -DNCURSES -DPERL_POLLUTE" 

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdldoc
%{_mandir}/man1/PDL*
%{_mandir}/man1/pdl*
%{_mandir}/man3/PDL.*
%{_mandir}/man3/PDL::A*
%{_mandir}/man3/PDL::Ba*
%{_mandir}/man3/PDL::C*
%{_mandir}/man3/PDL::D*
%{_mandir}/man3/PDL::E*
%{_mandir}/man3/PDL::F*
%{_mandir}/man3/PDL::Ga*
%{_mandir}/man3/PDL::Im*
%{_mandir}/man3/PDL::IO::Misc*
%{_mandir}/man3/PDL::L*
%{_mandir}/man3/PDL::M*
%{_mandir}/man3/PDL::O*
%{_mandir}/man3/PDL::P*
%{_mandir}/man3/PDL::R*
%{_mandir}/man3/PDL::S*
%{_mandir}/man3/PDL::T*
%{_mandir}/man3/PDL::U*

%dir %{perl_sitearch}/PDL

%{perl_sitearch}/PDL.pm
%{perl_sitearch}/PDL/A*
%{perl_sitearch}/PDL/B*
%{perl_sitearch}/PDL/C*
%{perl_sitearch}/PDL/Da*
%{perl_sitearch}/PDL/Db*
%{perl_sitearch}/PDL/Del*
%{perl_sitearch}/PDL/Do*
%{perl_sitearch}/PDL/E*
%{perl_sitearch}/PDL/F*
%{perl_sitearch}/PDL/Ga*
%{perl_sitearch}/PDL/H*
%{perl_sitearch}/PDL/Im*
%{perl_sitearch}/PDL/IO/Misc*
%{perl_sitearch}/PDL/L*
%{perl_sitearch}/PDL/M*
%{perl_sitearch}/PDL/O*
%{perl_sitearch}/PDL/P*
%{perl_sitearch}/PDL/R*
%{perl_sitearch}/PDL/S*
%{perl_sitearch}/PDL/T*
%{perl_sitearch}/PDL/U*
%{perl_sitearch}/PDL/V*
%{perl_sitearch}/PDL/d*
%{perl_sitearch}/PDL/pdl*

%dir %{perl_sitearch}/PDL/Graphics

%dir %{perl_sitearch}/auto/PDL
%dir %{perl_sitearch}/auto/PDL/Graphics
%dir %{perl_sitearch}/auto/PDL/IO

%attr(-,root,root) %{perl_sitearch}/auto/PDL/Bad
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Complex
%attr(-,root,root) %{perl_sitearch}/auto/PDL/FFT
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Image2D
%attr(-,root,root) %{perl_sitearch}/auto/PDL/ImageRGB
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Ops
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Slices
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Ufunc
%attr(-,root,root) %{perl_sitearch}/auto/PDL/CallExt
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Core
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Fit
%attr(-,root,root) %{perl_sitearch}/auto/PDL/ImageND
%attr(-,root,root) %{perl_sitearch}/auto/PDL/IO/Misc
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Math
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Primitive
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Tests

%files perldl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perldl
%{_mandir}/man1/perldl*
%{perl_sitearch}/PDL/perldl*

%files Graphics-TriD
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::Graphics::TriD.*
%{_mandir}/man3/PDL::Graphics::TriD::[A-SU-Z]*
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Graphics/TriD
%dir %{perl_sitearch}/PDL/Graphics/TriD
%{perl_sitearch}/PDL/Graphics/TriD/[A-SU-Z]*
%{perl_sitearch}/PDL/Graphics/TriD/Te*
%{perl_sitearch}/PDL/Graphics/VRML*

%files Graphics-TriD-Tk
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::Graphics::TriD::Tk*
%{perl_sitearch}/PDL/Graphics/TriD/Tk*

%files Graphics-PGPLOT
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::Graphics2D*
%{_mandir}/man3/PDL::Graphics::PGPLOT*
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Graphics/PGPLOT
%{perl_sitearch}/PDL/Graphics/PGPLOT*
%{perl_sitearch}/PDL/Graphics2D*

%files Graphics-LUT
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::Graphics::LUT*
%{perl_sitearch}/PDL/Graphics/LUT*

%files Graphics-IIS
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::Graphics::IIS*
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Graphics/IIS
%{perl_sitearch}/PDL/Graphics/IIS*

%files Graphics-OpenGL
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::Graphics::OpenGL*
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Graphics/OpenGL*
%{perl_sitearch}/PDL/Graphics/OpenGL*

%files IO-Browser
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::Browser*
%attr(-,root,root) %{perl_sitearch}/auto/PDL/IO/Browser
%{perl_sitearch}/PDL/IO/Browser*

%files IO-FastRaw
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::FastRaw*
%{perl_sitearch}/PDL/IO/FastRaw*

%files IO-FlexRaw
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::FlexRaw*
%{perl_sitearch}/PDL/IO/FlexRaw*

%files IO-NDF
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::NDF*
%{perl_sitearch}/PDL/IO/NDF*

%files IO-Pic
%defattr(644,root,root,755)
%{perl_sitearch}/PDL/IO/Pic*

%files IO-Pnm
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::Pnm*
%attr(-,root,root) %{perl_sitearch}/auto/PDL/IO/Pnm
%{perl_sitearch}/PDL/IO/Pnm*

%files Demos
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::BAD*
%{perl_sitearch}/PDL/Demos
