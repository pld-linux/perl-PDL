%include	/usr/lib/rpm/macros.perl
%define		__find_provides	%{_builddir}/PDL-%{version}/find-perl-provides
%define		__find_requires %{_builddir}/PDL-%{version}/find-perl-requires
Summary:	perlDL - efficient numerical computing for Perl
Summary(pl):	perlDL - wydajne obliczenia numeryczne w Perlu
Name:		perl-PDL
Version:	2.2
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
The perlDL project aims to turn Perl into an efficient numerical language
for scientific computing. The PDL module gives standard Perl the ability to
COMPACTLY store and SPEEDILY manipulate the large N-dimensional data sets
which are the bread and butter of scientific computing, i.e. C<$a=$b+$c>
can add two 2048x2048 images in only a fraction of a second.

%description -l pl
Modu³ perlDL rozszerza mo¿liwo¶ci Perla o funkcje do obliczeñ numerycznych.
Umo¿liwia przechowywanie oraz szybkie manipulowanie du¿ymi n-wymiarowymi
zbiorami danych, które s± chlebem powszednim naukowych obliczeñ, np.:
C<$a=$b+$c> dodaje dwie bitmapy rozmiaru 2048x2048 w u³amku sekundy.

%package perldl
Summary:	PDL shell
Summary(pl):	Pow³oka PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description perldl
The program perldl is a simple shell (written in perl) for interactive use
of PDL.  perl/PDL commands can simply be typed in - and edited if you have
appropriate version of the ReadLines and ReadKeys modules installed.  In
that case perldl also supports a history mechanism.

%description -l pl perldl
Program perldl jest prost± pow³ok± napisan± w Perlu do interaktywnego
wykonywania funkcji modu³u PDL. Komendy Perla lub PDL mog± byæ w prosty
sposób wprowadzane, a tak¿e edytowane je¶li masz zainstalowan± odpowiedni±
wersjê modu³ó ReadLines oraz ReadKeys. W tym ostatnim przypadku perldl
wspiera mechanizm historii komend.

%package Graphics-TriD
Summary:	PDL 3D interface
Summary(pl):	Interfejs 3D dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description Graphics-TriD
This module implements a generic 3D plotting interface for PDL.  Points,
lines and surfaces (among other objects) are supported.

With OpenGL, it is easy to manipulate the resulting 3D objects with the
mouse in real time - this helps data visualization a lot.

With VRML, you can generate objects for everyone to see with e.g.  Silicon
Graphics' Cosmo Player. You can find out more about VRML at
`http://vrml.sgi.com/' or `http://www.vrml.org/'

%description -l pl Graphics-TriD
Modu³ ten implementuje podstawowy interfejs 3D dla PDL. Dostêpne s± - w¶ród innych
obiektów - punkty, linie oraz powierzchnie.

Za pomoc± OpenGL, stworzonymi obiektami 3D mo¿na ³atwo manipulowaæ w czasie
rzeczywistym za pomoc± myszy, co bardzo wspomaga wizualizacjê danych.

Mo¿esz te¿ generowaæ obiekty w formacie VRML, które mog± byæ ogl±dane
przez inne osoby za pomoc± np.: programu Cosmo Player firmy Silicon Graphics.
Wiêcej na temat VRML mo¿esz znale¼æ pod adresami http://vrml.sgi.com/
lub http://www.vrml.org/.

%package Graphics-TriD-Tk
Summary:	A Tk widget interface to the PDL-Graphics-TriD
Summary(pl):	Kontrolka interfejsu Tk dla PDL-Graphics-TriD
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description Graphics-TriD-Tk
The widget is composed of a Frame and the Display device of the TriD
output.  It inherits all of the attributes of a Tk Frame.  All of the
events associated with this window are handled through Tk with the
exception of the <expose> event which must be handled by TriD because the
Frame is never exposed.  Default mouse bindings, defined for button1 and
button3, control TriD object orientation and size respectively.

%description -l pl Graphics-TriD-Tk
Kontrolka ta sk³ada siê z obiektu Frame oraz urz±dzenia Display
modu³u TriD. Dziedziczy ona wszystkie atrybuty obiektu Tk Frame.
Wszystkie zdarzenia skojarzone z tym oknem kontrolki s± obs³ugiwane
za pomoc± Tk za wyj±tkiem zdarzenia <expose>, które musi byæ obs³u¿one
przez modu³ TriD, poniewa¿ obiekt Frame nie jest nigdy wy¶wietlany.
Za pomoc± przycisków myszki mo¿na kontrolowaæ widok obiektu
(przycisk pierwszy) oraz jego rozmiar (przycisk trzeci).

%package Graphics-PGPLOT
Summary:	PGPLOT enhanced interface for PDL
Summary(pl):	Rozszerzony interfejs biblioteki PGPLOT dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description Graphics-PGPLOT
`PDL::Graphics::PGPLOT' is a convenience interface to the PGPLOT commands,
implemented using the object oriented PGPLOT plotting package in the
PDL::Graphics::PGPLOT::Window manpage. See the documentation for that
package for in-depth information about the usage of these commands and the
options they accept.

%description -l pl Graphics-PGPLOT
Modu³ ten jest interfejsem do komend biblioteki PGPLOT. Jest ona
zaimplementowany za pomoc± obiektowo zorientowanego pakietu PGPLOT
(spójrz do manuala modu³u PDL::Graphics::PGPLOT::Window).

%package Graphics-IIS
Summary:	Display PDL images on IIS devices (saoimage/ximtool)
Summary(pl):	Wy¶wietlanie grafiki PDL na urz±dzeniach IIS (saoimage/ximtool)
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description Graphics-IIS
Display PDL images on IIS devices (saoimage/ximtool).

%description -l pl Graphics-IIS
Wy¶wietlanie grafiki PDL na urz±dzeniach IIS (saoimage/ximtool).

%package Graphics-LUT
Summary:	Provides access to a number of look-up tables for PDL
Summary(pl):	N/A
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description Graphics-LUT
Provides access to a number of look-up tables for PDL.

%description -l pl Graphics-LUT

%package Graphics-OpenGL
Summary:	PDL interface to the OpenGL graphics library
Summary(pl):	Interfejs OpenGL dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description Graphics-OpenGL
PDL interface to the OpenGL graphics library.

%description -l pl Graphics-OpenGL
Interfejs OpenGL dla PDL.

%package IO-Browser
Summary:	2D data browser for PDL
Summary(pl):	Przegl±darka danych 2D dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description IO-Browser
2D data browser for PDL.

%description -l pl IO-Browser
Przegl±darka danych 2D dla PDL.

%package IO-FastRaw
Summary:	A simple, fast and convenient IO format for PDL
Summary(pl):	Prosty, szybki i wygodny format wej¶cia/wyj¶cia dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description IO-FastRaw
A simple, fast and convenient IO format for PDL.

%description -l pl IO-FastRaw
Prosty, szybki i wygodny format wej¶cia/wyj¶cia dla PDL.

%package IO-FlexRaw
Summary:	 A flexible binary IO format for PDL
Summary(pl):	Elastyczny binarny format wej¶cia/wyj¶cia dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description IO-FlexRaw
A flexible binary IO format for PDL.

%description -l pl IO-FlexRaw
Elastyczny binarny format wej¶cia/wyj¶cia dla PDL.

%package IO-NDF
Summary:	Starlink N-dimensional data structures for PDL
Summary(pl):	Wsparcie dla n-wymiarowych struktur danych firmy Starlink dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description IO-NDF
Starlink N-dimensional data structures for PDL.

%description -l pl IO-NDF
Wsparcie dla n-wymiarowych struktur danych firmy Starlink dla PDL.

%package IO-Pic
Summary:	IO-Pic
Summary(pl):	IO-Pic
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Requires:	netpbm

%description IO-Pic
IO-Pic.

%description -l pl IO-Pic
IO-Pic.

%package IO-Pnm
Summary:	PNM format IO for PDL
Summary(pl):	Wsparcie dla formatu PNM dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description IO-Pnm
PNM format IO for PDL.

%description -l pl IO-Pnm
Wsparcie dla formatu PNM dla PDL.

%package Demos
Summary:	PDL demos
Summary(pl):	Przyk³adowe skrypty z u¿yciem PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl

%description Demos
PDL demos.

%description -l pl Demos
Przyk³adowe skrypty z u¿yciem PDL.

%prep
%setup  -q -n PDL-%{version}
%patch0 -p1 
%patch1 -p1

chmod +x find-*

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS} \
	-I%{_includedir}/ncurses -DNCURSES -DPERL_POLLUTE" 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdldoc
%dir %{perl_sitearch}/PDL

%{perl_sitearch}/PDL.pm
%{perl_sitearch}/PDL/AutoLoader.pm
%{perl_sitearch}/PDL/Bad.pm
%{perl_sitearch}/PDL/Basic.pm
%{perl_sitearch}/PDL/CallExt.pm
%{perl_sitearch}/PDL/Char.pm
%{perl_sitearch}/PDL/Complex.pm
%{perl_sitearch}/PDL/Config.pm
%{perl_sitearch}/PDL/Core
%{perl_sitearch}/PDL/Core.pm
%{perl_sitearch}/PDL/Dbg.pm
%{perl_sitearch}/PDL/Doc
%{perl_sitearch}/PDL/Doc.pm
%{perl_sitearch}/PDL/Exporter.pm
%{perl_sitearch}/PDL/FFT.pm
%{perl_sitearch}/PDL/Filter
%{perl_sitearch}/PDL/Fit
%{perl_sitearch}/PDL/Func.pm
%{perl_sitearch}/PDL/Gaussian.pm
%dir %{perl_sitearch}/PDL/Graphics
%{perl_sitearch}/PDL/Graphics2D.pm
%{perl_sitearch}/PDL/Image2D.pm
%{perl_sitearch}/PDL/ImageND.pm
%{perl_sitearch}/PDL/ImageRGB.pm
%{perl_sitearch}/PDL/IO
%{perl_sitearch}/PDL/LiteF.pm
%{perl_sitearch}/PDL/Lite.pm
%{perl_sitearch}/PDL/Math.pm
%{perl_sitearch}/PDL/Matrix.pm
%{perl_sitearch}/PDL/Opt
%{perl_sitearch}/PDL/Ops.pm
%{perl_sitearch}/PDL/Options.pm
%{perl_sitearch}/PDL/PP
%{perl_sitearch}/PDL/PP.pm
%{perl_sitearch}/PDL/Primitive.pm
%{perl_sitearch}/PDL/Pod
%{perl_sitearch}/PDL/Reduce.pm
%{perl_sitearch}/PDL/Slices.pm
%{perl_sitearch}/PDL/Tests.pm
%{perl_sitearch}/PDL/Types.pm
%{perl_sitearch}/PDL/Ufunc.pm
%{perl_sitearch}/PDL/Version.pm
%{perl_sitearch}/PDL/default.perldlrc
%{perl_sitearch}/PDL/pdl*

%dir %{perl_sitearch}/auto/PDL
%dir %{perl_sitearch}/auto/PDL/Bad
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Bad/*.so
%dir %{perl_sitearch}/auto/PDL/Complex
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Complex/*.so
%dir %{perl_sitearch}/auto/PDL/FFT
%attr(755,root,root) %{perl_sitearch}/auto/PDL/FFT/*so
%dir %{perl_sitearch}/auto/PDL/Graphics
%dir %{perl_sitearch}/auto/PDL/IO

%dir %{perl_sitearch}/auto/PDL/Image2D
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Image2D/*.so
%dir %{perl_sitearch}/auto/PDL/ImageRGB
%attr(755,root,root) %{perl_sitearch}/auto/PDL/ImageRGB/*.so
%dir %{perl_sitearch}/auto/PDL/Ops
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Ops/*.so
%dir %{perl_sitearch}/auto/PDL/Slices
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Slices/*.so
%dir %{perl_sitearch}/auto/PDL/Ufunc
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Ufunc/*.so
%dir %{perl_sitearch}/auto/PDL/CallExt
%attr(755,root,root) %{perl_sitearch}/auto/PDL/CallExt/*.so
%dir %{perl_sitearch}/auto/PDL/Core
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Core/*.so
%dir %{perl_sitearch}/auto/PDL/Fit
%dir %{perl_sitearch}/auto/PDL/Fit/Gaussian
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Fit/Gaussian/*.so
%dir %{perl_sitearch}/auto/PDL/ImageND
%attr(755,root,root) %{perl_sitearch}/auto/PDL/ImageND/*.so
%dir %{perl_sitearch}/auto/PDL/IO/Misc
%attr(755,root,root) %{perl_sitearch}/auto/PDL/IO/Misc/*.so
%dir %{perl_sitearch}/auto/PDL/Math
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Math/*.so
%dir %{perl_sitearch}/auto/PDL/Primitive
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Primitive/*.so
%dir %{perl_sitearch}/auto/PDL/Tests
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Tests/*.so

%{_mandir}/man1/PDL*
%{_mandir}/man1/pdl.*
%{_mandir}/man1/pdldoc.*
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

%files perldl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perldl
%{_mandir}/man1/perldl*
%{perl_sitearch}/PDL/perldl*

%files Graphics-TriD
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::Graphics::TriD.*
%{_mandir}/man3/PDL::Graphics::TriD::[A-SU-Z]*
%dir %{perl_sitearch}/auto/PDL/Graphics/TriD
%dir %{perl_sitearch}/auto/PDL/Graphics/TriD/Rout
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Graphics/TriD/Rout/*.so
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
%dir %{perl_sitearch}/auto/PDL/Graphics/PGPLOT
%dir %{perl_sitearch}/auto/PDL/Graphics/PGPLOT/Window
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Graphics/PGPLOT/Window/*.so
%{perl_sitearch}/PDL/Graphics/PGPLOT*
%{perl_sitearch}/PDL/Graphics2D*

%files Graphics-LUT
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::Graphics::LUT*
%{perl_sitearch}/PDL/Graphics/LUT*

%files Graphics-IIS
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::Graphics::IIS*
%dir %{perl_sitearch}/auto/PDL/Graphics/IIS
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Graphics/IIS/*.so
%{perl_sitearch}/PDL/Graphics/IIS*

%files Graphics-OpenGL
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::Graphics::OpenGL*
%dir %{perl_sitearch}/auto/PDL/Graphics/OpenGL*
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Graphics/OpenGL*/*so
%{perl_sitearch}/PDL/Graphics/OpenGL*

%files IO-Browser
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::Browser*
%dir %{perl_sitearch}/auto/PDL/IO/Browser
%attr(755,root,root) %{perl_sitearch}/auto/PDL/IO/Browser/*.so
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
%dir %{perl_sitearch}/auto/PDL/IO/Pnm
%attr(755,root,root) %{perl_sitearch}/auto/PDL/IO/Pnm/*.so
%{perl_sitearch}/PDL/IO/Pnm*

%files Demos
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::BAD*
%{perl_sitearch}/PDL/Demos
