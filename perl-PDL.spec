#
# Conditional build:
%bcond_without  karma	# build package with PDL::Graphics::Karma modules
%bcond_without  html	# don't generate package with PDL documentation in HTML
%bcond_with	tests	# perform "make test"
			# require a valid DISPLAY
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PDL
Summary:	perlDL - efficient numerical computing for Perl
Summary(pl):	perlDL - wydajne obliczenia numeryczne w Perlu
Summary(pt_BR):	Módulo PDL para perl
Name:		perl-PDL
Version:	2.4.1
Release:	2
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	0d57eb5ccb4d9e63103622e1e1144793
Patch0:		%{name}-conf.patch
Patch1:		%{name}-dep.patch
Patch2:		%{name}-Makefile.PL.patch-dumb
Patch3:		%{name}-fftw-shared.patch
Patch4:		%{name}-WITH_IO_BROWSER.patch
Patch5:		%{name}-karma.patch
Patch6:		%{name}-vendorarch.patch
URL:		http://pdl.perl.org/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	fftw-devel >= 2.1.3-5
BuildRequires:	gsl-devel >= 1.3
%{?with_karma:BuildRequires:	karma-devel}
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	perl-ExtUtils-F77 >= 1.10
BuildRequires:	perl-Filter
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	perl-PGPLOT
BuildRequires:	perl-Tk
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-perldoc
BuildRequires:	plplot-devel >= 5.2.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1
%define		_noautoreq	'perl(local.perldlrc)'

%description
The perlDL project aims to turn Perl into an efficient numerical
language for scientific computing. The PDL module gives standard Perl
the ability to COMPACTLY store and SPEEDILY manipulate the large
N-dimensional data sets which are the bread and butter of scientific
computing, i.e. C<$a=$b+$c> can add two 2048x2048 images in only a
fraction of a second.

%description -l pl
Modu³ perlDL rozszerza mo¿liwo¶ci Perla o funkcje do obliczeñ
numerycznych. Umo¿liwia przechowywanie oraz szybkie manipulowanie
du¿ymi n-wymiarowymi zbiorami danych, które s± chlebem powszednim
naukowych obliczeñ, np.: C<$a=$b+$c> dodaje dwie bitmapy rozmiaru
2048x2048 w u³amku sekundy.

%description -l pt_BR
O projeto perlDL pretende tornar perl uma linguagem númerica eficiente
para computação científica. O módulo PDL dá ao perl a habilidade de
armazenar de forma compacta e manipular rapidamente grandes conjuntos
de dados de N dimensões que são muito comuns em computação científica.
Ex. $a=$b+$c pode adicionar imagens de 2048x2048 em apenas uma fração
de segundo.

%package perldl
Summary:	PDL shell
Summary(pl):	Pow³oka PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description perldl
The program perldl is a simple shell (written in perl) for interactive
use of PDL. perl/PDL commands can simply be typed in - and edited if
you have appropriate version of the ReadLines and ReadKeys modules
installed. In that case perldl also supports a history mechanism.

%description perldl -l pl
Program perldl jest prost± pow³ok± napisan± w Perlu do interaktywnego
wykonywania funkcji modu³u PDL. Komendy Perla lub PDL mog± byæ w
prosty sposób wprowadzane, a tak¿e edytowane je¶li masz zainstalowan±
odpowiedni± wersjê modu³ó ReadLines oraz ReadKeys. W tym ostatnim
przypadku perldl wspiera mechanizm historii komend.

%package docs
Summary:	Supplied extra documentation for PDL::* perl modules
Summary(pl):	Dodatkowo dostarczona dokumentacja do modu³ów perla PDL::*
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description docs
Additional, supplied by authors, documentation to all PDL::* modules.

%description docs -l pl
Dodatkowa, dostarczona przez autorów, dokumentacja do modu³ów PDL::*.

%package docs-HTML
Summary:	Supplied extra documentation for PDL::* perl modules in HTML format
Summary(pl):	Dodatkowo dostarczona dokumentacja w HTML-u do modu³ów perla PDL::*
Group:		Development/Languages/Perl
# for install dir
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description docs-HTML
Additional, supplied by authors, documentation in HTML format to all
PDL::* modules.

%description docs-HTML -l pl
Dodatkowa, dostarczona przez autorów, dokumentacja do modu³ów PDL::*,
w formacie HTML.

%package Graphics-IIS
Summary:	Display PDL images on IIS devices (saoimage/ximtool)
Summary(pl):	Wy¶wietlanie grafiki PDL na urz±dzeniach IIS (saoimage/ximtool)
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Graphics-IIS
Display PDL images on IIS devices (saoimage/ximtool).

%description Graphics-IIS -l pl
Wy¶wietlanie grafiki PDL na urz±dzeniach IIS (saoimage/ximtool).

%package Graphics-Karma
Summary:	Interface to Karma visualisation applications
Summary(pl):	Interfejs do aplikacji wizualizuj±cych Karma
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Graphics-Karma
PDL::Graphics::Karma is an interface to Karma visualisation
applications. It can send PDL 2D/3D data to kview, xray, kslice_3d,
etc.

%description Graphics-Karma -l pl
PDL::Graphics::Karma to interfejs do aplikacji wizualizuj±cych Karma.
Mo¿e wysy³aæ dane 2D i 3D do kview, xray, kslice_3d itp.

%package Graphics-LUT
Summary:	Provides access to a number of look-up tables for PDL
Summary(pl):	Dostêp do tablic kolorów dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Graphics-LUT
Provides access to a number of look-up tables for PDL.

%description Graphics-LUT -l pl
Modu³ zapewnia dostêp do ró¿nych tablic kolorów (palet) dla PDL.

%package Graphics-OpenGL
Summary:	PDL interface to the OpenGL graphics library
Summary(pl):	Interfejs OpenGL dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Graphics-OpenGL
PDL interface to the OpenGL graphics library.

%description Graphics-OpenGL -l pl
Interfejs OpenGL dla PDL.

%package Graphics-PGPLOT
Summary:	PGPLOT enhanced interface for PDL
Summary(pl):	Rozszerzony interfejs biblioteki PGPLOT dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Graphics-PGPLOT
`PDL::Graphics::PGPLOT' is a convenience interface to the PGPLOT
commands, implemented using the object oriented PGPLOT plotting
package in the PDL::Graphics::PGPLOT::Window manpage. See the
documentation for that package for in-depth information about the
usage of these commands and the options they accept.

%description Graphics-PGPLOT -l pl
Modu³ ten jest interfejsem do komend biblioteki PGPLOT. Jest ona
zaimplementowany za pomoc± obiektowo zorientowanego pakietu PGPLOT
(spójrz do manuala modu³u PDL::Graphics::PGPLOT::Window).

%package Graphics-PLplot
Summary:	PDL::Graphics::PLplot - interface to the PLplot plotting library
Summary(pl):	PDL::Graphics::PLplot - interfejs do biblioteki rysuj±cej PLplot
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Graphics-PLplot
PDL::Graphics::PLplot is the PDL interface to the PLplot graphics
library. It is designed to be simple and light weight with a familiar
'perlish' Object Oriented interface.

%description Graphics-PLplot -l pl
PDL::Graphics::PLplot to interfejs PLD do biblioteki graficznej
PLplot. Jest zaprojektowany tak, aby by³ prosty i lekki ze znajomym
perlowatym zorientowanym obiektowo interfejsem.

%package Graphics-TriD
Summary:	PDL 3D interface
Summary(pl):	Interfejs 3D dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-Graphics-OpenGL = %{epoch}:%{version}-%{release}
Requires:	%{name}-IO-Pic = %{epoch}:%{version}-%{release}

%description Graphics-TriD
This module implements a generic 3D plotting interface for PDL.
Points, lines and surfaces (among other objects) are supported.

With OpenGL, it is easy to manipulate the resulting 3D objects with
the mouse in real time - this helps data visualization a lot.

With VRML, you can generate objects for everyone to see with e.g.
Silicon Graphics' Cosmo Player. You can find out more about VRML at
`http://vrml.sgi.com/' or `http://www.vrml.org/'

%description Graphics-TriD -l pl
Modu³ ten implementuje podstawowy interfejs 3D dla PDL. Dostêpne s± -
w¶ród innych obiektów - punkty, linie oraz powierzchnie.

Za pomoc± OpenGL, stworzonymi obiektami 3D mo¿na ³atwo manipulowaæ w
czasie rzeczywistym za pomoc± myszy, co bardzo wspomaga wizualizacjê
danych.

Mo¿esz te¿ generowaæ obiekty w formacie VRML, które mog± byæ ogl±dane
przez inne osoby za pomoc± np.: programu Cosmo Player firmy Silicon
Graphics. Wiêcej na temat VRML mo¿esz znale¼æ pod adresami
http://vrml.sgi.com/ lub http://www.vrml.org/.

%package Graphics-TriD-Tk
Summary:	A Tk widget interface to the PDL-Graphics-TriD
Summary(pl):	Kontrolka interfejsu Tk dla PDL-Graphics-TriD
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-Graphics-OpenGL = %{epoch}:%{version}-%{release}
Requires:	%{name}-Graphics-TriD = %{epoch}:%{version}-%{release}

%description Graphics-TriD-Tk
The widget is composed of a Frame and the Display device of the TriD
output. It inherits all of the attributes of a Tk Frame. All of the
events associated with this window are handled through Tk with the
exception of the <expose> event which must be handled by TriD because
the Frame is never exposed. Default mouse bindings, defined for
button1 and button3, control TriD object orientation and size
respectively.

%description Graphics-TriD-Tk -l pl
Kontrolka ta sk³ada siê z obiektu Frame oraz urz±dzenia Display modu³u
TriD. Dziedziczy ona wszystkie atrybuty obiektu Tk Frame. Wszystkie
zdarzenia skojarzone z tym oknem kontrolki s± obs³ugiwane za pomoc± Tk
za wyj±tkiem zdarzenia <expose>, które musi byæ obs³u¿one przez modu³
TriD, poniewa¿ obiekt Frame nie jest nigdy wy¶wietlany. Za pomoc±
przycisków myszki mo¿na kontrolowaæ widok obiektu (przycisk pierwszy)
oraz jego rozmiar (przycisk trzeci).

%package IO-Browser
Summary:	2D data browser for PDL
Summary(pl):	Przegl±darka danych 2D dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description IO-Browser
2D data browser for PDL.

%description -l pl IO-Browser
Przegl±darka danych 2D dla PDL.

%package IO-FastRaw
Summary:	A simple, fast and convenient IO format for PDL
Summary(pl):	Prosty, szybki i wygodny format wej¶cia/wyj¶cia dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description IO-FastRaw
A simple, fast and convenient IO format for PDL.

%description IO-FastRaw -l pl
Prosty, szybki i wygodny format wej¶cia/wyj¶cia dla PDL.

%package IO-FlexRaw
Summary:	A flexible binary IO format for PDL
Summary(pl):	Elastyczny binarny format wej¶cia/wyj¶cia dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description IO-FlexRaw
A flexible binary IO format for PDL.

%description IO-FlexRaw -l pl
Elastyczny binarny format wej¶cia/wyj¶cia dla PDL.

%package IO-NDF
Summary:	Starlink N-dimensional data structures for PDL
Summary(pl):	Wsparcie dla n-wymiarowych struktur danych firmy Starlink dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description IO-NDF
Starlink N-dimensional data structures for PDL.

%description IO-NDF -l pl
Wsparcie dla n-wymiarowych struktur danych firmy Starlink dla PDL.

%package IO-Pic
Summary:	Image I/O for PDL based on the netpbm package
Summary(pl):	Obs³uga obrazków dla PDL oparta na pakiecie netpbm
Group:		Development/Languages/Perl
Requires:	netpbm
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-IO-Pnm = %{epoch}:%{version}-%{release}

%description IO-Pic
This package implements I/O for a number of popular image formats by
exploiting the xxxtopnm and pnmtoxxx converters from the netpbm
package.

%description IO-Pic -l pl
Pakiet daje mo¿liwo¶æ czytania i zapisywania obrazków w wielu
formatach poprzez wykorzystywanie konwerterów xxxtopnm i pnmtoxxx z
pakietu netpbm.

%package IO-Pnm
Summary:	PNM format IO for PDL
Summary(pl):	Wsparcie dla formatu PNM dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description IO-Pnm
PNM format IO for PDL.

%description IO-Pnm -l pl
Wsparcie dla formatu PNM dla PDL.

%package IO-Storable
Summary:	Helper functions to make PDL usable with Storable
Summary(pl):	Funkcje pomocnicze pozwalajace u¿ywaæ PDL ze Storable
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description IO-Storable
Helper functions to make PDL usable with Storable.

%description IO-Storable -l pl
Funkcje pomocnicze pozwalajace u¿ywaæ PDL wraz ze Storable.

%package Slatec
Summary:	PDL interface to the Slatec numerical programming library
Summary(pl):	Interfejs PDL do biblioteki numerycznej Slatec
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Slatec
PDL interface to the Slatec numerical programming library.

%description Slatec -l pl
Interfejs PDL do biblioteki numerycznej Slatec.

%package GSL
Summary:	PDL interface to RNG and randist routines in GSL
Summary(pl):	Interfejs PDL do funkcji RNG i randist z biblioteki GSL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description GSL
Interface to the rng and randist packages present in the GNU
Scientific Library.

%description GSL -l pl
Interfejs do funkcji rng i randist z biblioteki GSL.

%package GSLSF
Summary:	PDL interface to GSL Special Functions
Summary(pl):	Interfejs PDL do funkcji specjalnych GSL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description GSLSF
PDL interface to GSL Special Functions.

%description GSLSF -l pl
Interfejs PDL do funkcji specjalnych GSL.

%package Demos
Summary:	PDL demos
Summary(pl):	Przyk³adowe skrypty z u¿yciem PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-Graphics-LUT = %{epoch}:%{version}-%{release}
Requires:	%{name}-Graphics-PGPLOT = %{epoch}:%{version}-%{release}
Requires:	%{name}-Graphics-TriD = %{epoch}:%{version}-%{release}
Requires:	%{name}-Graphics-TriD-Tk = %{epoch}:%{version}-%{release}

%description Demos
PDL demos.

%description Demos -l pl
Przyk³adowe skrypty z u¿yciem PDL.

%prep
%setup -q -n %{pdir}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%{?with_karma:%patch5 -p1}
%patch6 -p1

%{__perl} -pi -e 's/\b(pdlpp_postamble)\b/$1_int/g' Graphics/PLplot/Makefile.PL
# g77 flags for compiling Slatec:
%{__perl} -pi -e 's@\) \$mycflags s@\) %{rpmcflags} -fPIC s@' Lib/Slatec/Makefile.PL

%{__perl} -pi -e "s@(FFTW_LIBS.*)'/lib','/usr/lib','/usr/local/lib'@\$1'/usr/%{_lib}'@" perldl.conf
%{__perl} -pi -e "s@(OPENGL_LIBS.*)'-L/usr/X11R6/lib@\$1'-L/usr/X11R6/%{_lib}@" perldl.conf
%{__perl} -pi -e "s@(WHERE_KARMA.*)\"/usr/lib/karma@\$1\"/usr/%{_lib}/karma@" perldl.conf
%{__perl} -pi -e "s@(WHERE_PLPLOT_LIBS.*)undef@\$1'/usr/%{_lib}'@" perldl.conf

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags} -I/usr/include/ncurses -DNCURSES -DPERL_POLLUTE"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# perl script to regenerate pdldoc database
install Doc/scantree.pl $RPM_BUILD_ROOT%{perl_vendorarch}/PDL/scantree.pl

# some manuals have wrong names - this can be fixed in "Makefile.PL"s or here:
cd $RPM_BUILD_ROOT%{_mandir}/man3
mv -f PDL::Dev.3pm		PDL::Core::Dev.3pm
mv -f PDL::Linear.3pm		PDL::Filter::Linear.3pm
mv -f PDL::LinPred.3pm		PDL::Filter::LinPred.3pm
mv -f PDL::LM.3pm		PDL::Fit::LM.3pm
mv -f PDL::Linfit.3pm 		PDL::Fit::Linfit.3pm
mv -f PDL::Polynomial.3pm	PDL::Fit::Polynomial.3pm
mv -f PDL::State.3pm		PDL::Graphics::State.3pm
mv -f Pdlpp.3pm			Inline::Pdlpp.3pm

# some man pages do not belong to the man1 section
cd $RPM_BUILD_ROOT%{_mandir}/man1
for i in PDL::*.1*; do
	mv $i ../man3/`echo $i | sed 's/\.1p\?$/.3/'`
done

%clean
rm -rf $RPM_BUILD_ROOT

%post docs
/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}

%post Graphics-IIS
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post Graphics-Karma
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post Graphics-LUT
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post Graphics-OpenGL
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post Graphics-PGPLOT
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post Graphics-PLplot
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post Graphics-TriD
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post Graphics-TriD-Tk
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post IO-Browser
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post IO-FastRaw
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post IO-FlexRaw
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post IO-NDF
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post IO-Pic
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post IO-Pnm
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post IO-Storable
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post Slatec
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post GSL
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post GSLSF
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post Demos
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun Graphics-IIS
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun Graphics-Karma
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun Graphics-LUT
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun Graphics-OpenGL
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun Graphics-PGPLOT
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun Graphics-PLplot
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun Graphics-TriD
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun Graphics-TriD-Tk
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun IO-Browser
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun IO-FastRaw
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun IO-FlexRaw
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun IO-NDF
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun IO-Pic
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun IO-Pnm
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun IO-Storable
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun Slatec
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun GSL
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun GSLSF
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun Demos
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pptemplate
%dir %{perl_vendorarch}/PDL

%{perl_vendorarch}/PDL.pm
%{perl_vendorarch}/PDL/AutoLoader.pm
%{perl_vendorarch}/PDL/Bad.pm
%{perl_vendorarch}/PDL/Basic.pm
%{perl_vendorarch}/PDL/CallExt.pm
%{perl_vendorarch}/PDL/Char.pm
%{perl_vendorarch}/PDL/Complex.pm
%{perl_vendorarch}/PDL/Config.pm
%{perl_vendorarch}/PDL/Core
%{perl_vendorarch}/PDL/Core.pm
%{perl_vendorarch}/PDL/Dbg.pm
%{perl_vendorarch}/PDL/DiskCache.pm
%{perl_vendorarch}/PDL/Doc
%{perl_vendorarch}/PDL/Doc.pm
%{perl_vendorarch}/PDL/Exporter.pm
%{perl_vendorarch}/PDL/FFT.pm
%{perl_vendorarch}/PDL/FFTW.pm
%dir %{perl_vendorarch}/PDL/Filter
%{perl_vendorarch}/PDL/Filter/Linear.pm
%dir %{perl_vendorarch}/PDL/Fit
%{perl_vendorarch}/PDL/Fit/Gaussian.pm
%{perl_vendorarch}/PDL/Func.pm
%dir %{perl_vendorarch}/PDL/Graphics
%{perl_vendorarch}/PDL/Graphics/State.pm
%{perl_vendorarch}/PDL/Image2D.pm
%{perl_vendorarch}/PDL/ImageND.pm
%{perl_vendorarch}/PDL/ImageRGB.pm
%dir %{perl_vendorarch}/PDL/IO
%{perl_vendorarch}/PDL/IO/Dumper.pm
%{perl_vendorarch}/PDL/IO/FITS.pm
%{perl_vendorarch}/PDL/IO/Misc.pm
%{perl_vendorarch}/PDL/LiteF.pm
%{perl_vendorarch}/PDL/Lite.pm
%{perl_vendorarch}/PDL/Lvalue.pm
%{perl_vendorarch}/PDL/Math.pm
%{perl_vendorarch}/PDL/MatrixOps.pm
%{perl_vendorarch}/PDL/NiceSlice.pm
%{perl_vendorarch}/PDL/Opt
%{perl_vendorarch}/PDL/Ops.pm
%{perl_vendorarch}/PDL/Options.pm
%{perl_vendorarch}/PDL/PP
%{perl_vendorarch}/PDL/PP.pm
%{perl_vendorarch}/PDL/Primitive.pm
%{perl_vendorarch}/PDL/Pod
%{perl_vendorarch}/PDL/Reduce.pm
%{perl_vendorarch}/PDL/Slices.pm
%{perl_vendorarch}/PDL/Tests.pm
# maybe separate PDL::Transform? (~500kB)
%{perl_vendorarch}/PDL/Transform.pm
%{perl_vendorarch}/PDL/Transform
%{perl_vendorarch}/PDL/Types.pm
%{perl_vendorarch}/PDL/Ufunc.pm
%{perl_vendorarch}/PDL/Version.pm
%{perl_vendorarch}/PDL/default.perldlrc

%dir %{perl_vendorarch}/auto/PDL
%dir %{perl_vendorarch}/auto/PDL/Bad
%{perl_vendorarch}/auto/PDL/Bad/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Bad/*.so
%dir %{perl_vendorarch}/auto/PDL/Complex
%{perl_vendorarch}/auto/PDL/Complex/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Complex/*.so
%dir %{perl_vendorarch}/auto/PDL/FFT
%{perl_vendorarch}/auto/PDL/FFT/*bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/FFT/*so
%dir %{perl_vendorarch}/auto/PDL/FFTW
%{perl_vendorarch}/auto/PDL/FFTW/*bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/FFTW/*so
%dir %{perl_vendorarch}/auto/PDL/Graphics
%dir %{perl_vendorarch}/auto/PDL/IO

%dir %{perl_vendorarch}/auto/PDL/Image2D
%{perl_vendorarch}/auto/PDL/Image2D/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Image2D/*.so
%dir %{perl_vendorarch}/auto/PDL/ImageRGB
%{perl_vendorarch}/auto/PDL/ImageRGB/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/ImageRGB/*.so
%dir %{perl_vendorarch}/auto/PDL/Ops
%{perl_vendorarch}/auto/PDL/Ops/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Ops/*.so
%dir %{perl_vendorarch}/auto/PDL/Slices
%{perl_vendorarch}/auto/PDL/Slices/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Slices/*.so
%dir %{perl_vendorarch}/auto/PDL/Ufunc
%{perl_vendorarch}/auto/PDL/Ufunc/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Ufunc/*.so
%dir %{perl_vendorarch}/auto/PDL/CallExt
%{perl_vendorarch}/auto/PDL/CallExt/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/CallExt/*.so
%dir %{perl_vendorarch}/auto/PDL/Core
%{perl_vendorarch}/auto/PDL/Core/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Core/*.so
%dir %{perl_vendorarch}/auto/PDL/Fit
%dir %{perl_vendorarch}/auto/PDL/Fit/Gaussian
%{perl_vendorarch}/auto/PDL/Fit/Gaussian/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Fit/Gaussian/*.so
%dir %{perl_vendorarch}/auto/PDL/ImageND
%{perl_vendorarch}/auto/PDL/ImageND/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/ImageND/*.so
%dir %{perl_vendorarch}/auto/PDL/IO/Misc
%{perl_vendorarch}/auto/PDL/IO/Misc/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/IO/Misc/*.so
%dir %{perl_vendorarch}/auto/PDL/Math
%{perl_vendorarch}/auto/PDL/Math/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Math/*.so
%dir %{perl_vendorarch}/auto/PDL/MatrixOps
%{perl_vendorarch}/auto/PDL/MatrixOps/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/MatrixOps/*.so
%dir %{perl_vendorarch}/auto/PDL/Primitive
%{perl_vendorarch}/auto/PDL/Primitive/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Primitive/*.so
%dir %{perl_vendorarch}/auto/PDL/Tests
%{perl_vendorarch}/auto/PDL/Tests/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Tests/*.so
%dir %{perl_vendorarch}/auto/PDL/Transform
%{perl_vendorarch}/auto/PDL/Transform/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Transform/*.so

%{perl_vendorarch}/Inline/Pdlpp.pm

%{_mandir}/man1/pdl.1*
%{_mandir}/man1/pptemplate.1*
%{_mandir}/man3/Inline::Pdlpp.3pm*
%{_mandir}/man3/PDL.*
%{_mandir}/man3/PDL::[AC-ELO-RTU]*
%{_mandir}/man3/PDL::Ba*
%{_mandir}/man3/PDL::FAQ*
%{_mandir}/man3/PDL::FFT*
%{_mandir}/man3/PDL::Filter::Linear*
%{_mandir}/man3/PDL::Fit::Gaussian*
%{_mandir}/man3/PDL::Func.3pm*
%{_mandir}/man3/PDL::Graphics::State.3pm*
%{_mandir}/man3/PDL::I[mn]*
%{_mandir}/man3/PDL::IO::FITS.3pm*
%{_mandir}/man3/PDL::IO::Misc*
%{_mandir}/man3/PDL::Math*
%{_mandir}/man3/PDL::MatrixOps.3pm*
%{_mandir}/man3/PDL::NiceSlice.3pm*
%{_mandir}/man3/PDL::Slices*
%{_mandir}/man3/PDL::pptemplate.3pm*

%files docs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdldoc
%attr(755,root,root) %{perl_vendorarch}/PDL/scantree.pl
%ghost %{perl_vendorarch}/PDL/pdldoc.db
%doc %{perl_vendorarch}/PDL/*.pod
%{_mandir}/man1/pdldoc.1*

%if %{with html}
%files docs-HTML
%defattr(644,root,root,755)
%doc %{perl_vendorarch}/PDL/HtmlDocs
%endif

%files perldl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perldl
%{_mandir}/man1/perldl*

%files Graphics-IIS
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/Graphics/IIS*
%dir %{perl_vendorarch}/auto/PDL/Graphics/IIS
%{perl_vendorarch}/auto/PDL/Graphics/IIS/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Graphics/IIS/*.so
%{_mandir}/man3/PDL::Graphics::IIS*

%if %{with karma}
%files Graphics-Karma
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/Graphics/Karma.pm
%dir %{perl_vendorarch}/auto/PDL/Graphics/Karma
%{perl_vendorarch}/auto/PDL/Graphics/Karma/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Graphics/Karma/*.so
%{_mandir}/man3/PDL::Graphics::Karma*
%endif

%files Graphics-LUT
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/Graphics/LUT*
%{_mandir}/man3/PDL::Graphics::LUT*

%files Graphics-OpenGL
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/Graphics/OpenGL*
%dir %{perl_vendorarch}/auto/PDL/Graphics/OpenGL*
%{perl_vendorarch}/auto/PDL/Graphics/OpenGL*/*bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Graphics/OpenGL*/*so
%{_mandir}/man3/PDL::Graphics::OpenGL*

%files Graphics-PGPLOT
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/Graphics/PGPLOT*
%{perl_vendorarch}/PDL/Graphics2D*
%dir %{perl_vendorarch}/auto/PDL/Graphics/PGPLOT
%dir %{perl_vendorarch}/auto/PDL/Graphics/PGPLOT/Window
%{perl_vendorarch}/auto/PDL/Graphics/PGPLOT/Window/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Graphics/PGPLOT/Window/*.so
%{_mandir}/man3/PDL::Graphics2D*
%{_mandir}/man3/PDL::Graphics::PGPLOT*

%files Graphics-PLplot
%defattr(644,root,root,755)
%doc Graphics/PLplot/{Changes,README}
%{perl_vendorarch}/PDL/Graphics/PLplot.pm
%dir %{perl_vendorarch}/auto/PDL/Graphics/PLplot
%{perl_vendorarch}/auto/PDL/Graphics/PLplot/PLplot.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Graphics/PLplot/PLplot.so
%{_mandir}/man3/PDL::Graphics::PLplot.3pm*

%files Graphics-TriD
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/PDL/Graphics/TriD
%{perl_vendorarch}/PDL/Graphics/TriD/[A-SU-Z]*
%{perl_vendorarch}/PDL/Graphics/TriD/Te*
%{perl_vendorarch}/PDL/Graphics/VRML*
%{perl_vendorarch}/PDL/Graphics/TriD.pm
%dir %{perl_vendorarch}/auto/PDL/Graphics/TriD
%dir %{perl_vendorarch}/auto/PDL/Graphics/TriD/Rout
%{perl_vendorarch}/auto/PDL/Graphics/TriD/Rout/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Graphics/TriD/Rout/*.so
%{_mandir}/man3/PDL::Graphics::TriD.*
%{_mandir}/man3/PDL::Graphics::TriD::[A-SU-Z]*

%files Graphics-TriD-Tk
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/Graphics/TriD/Tk*
%{_mandir}/man3/PDL::Graphics::TriD::Tk*

%files IO-Browser
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::Browser*
%dir %{perl_vendorarch}/auto/PDL/IO/Browser
%{perl_vendorarch}/auto/PDL/IO/Browser/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/IO/Browser/*.so
%{perl_vendorarch}/PDL/IO/Browser*

%files IO-FastRaw
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::FastRaw*
%{perl_vendorarch}/PDL/IO/FastRaw*

%files IO-FlexRaw
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::FlexRaw*
%{perl_vendorarch}/PDL/IO/FlexRaw*

%files IO-NDF
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::NDF*
%{perl_vendorarch}/PDL/IO/NDF*

%files IO-Pic
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/IO/Pic*

%files IO-Pnm
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::Pnm*
%dir %{perl_vendorarch}/auto/PDL/IO/Pnm
%{perl_vendorarch}/auto/PDL/IO/Pnm/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/IO/Pnm/*.so
%{perl_vendorarch}/PDL/IO/Pnm*

%files IO-Storable
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/IO/Storable.pm
%dir %{perl_vendorarch}/auto/PDL/IO/Storable
%{perl_vendorarch}/auto/PDL/IO/Storable/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/IO/Storable/*.so
%{_mandir}/man3/PDL::IO::Storable*

%files Slatec
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::Filter::LinPred*
%{_mandir}/man3/PDL::Fit::Linfit*
%{_mandir}/man3/PDL::Fit::LM*
%{_mandir}/man3/PDL::Fit::Polynomial*
%{_mandir}/man3/PDL::Gaussian*
%{_mandir}/man3/PDL::Matrix.3pm*
%{_mandir}/man3/PDL::Slatec*
%{perl_vendorarch}/PDL/Filter/LinPred.pm
%{perl_vendorarch}/PDL/Fit/Linfit.pm
%{perl_vendorarch}/PDL/Fit/LM.pm
%{perl_vendorarch}/PDL/Fit/Polynomial.pm
%{perl_vendorarch}/PDL/Gaussian.pm
%{perl_vendorarch}/PDL/Matrix.pm
%{perl_vendorarch}/PDL/Slatec.pm
%dir %{perl_vendorarch}/auto/PDL/Slatec
%{perl_vendorarch}/auto/PDL/Slatec/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Slatec/*.so

%files GSL
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/GSL
%dir %{perl_vendorarch}/auto/PDL/GSL
%dir %{perl_vendorarch}/auto/PDL/GSL/DIFF
%{perl_vendorarch}/auto/PDL/GSL/DIFF/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/GSL/DIFF/*.so
%dir %{perl_vendorarch}/auto/PDL/GSL/INTEG
%{perl_vendorarch}/auto/PDL/GSL/INTEG/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/GSL/INTEG/*.so
%dir %{perl_vendorarch}/auto/PDL/GSL/INTERP
%{perl_vendorarch}/auto/PDL/GSL/INTERP/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/GSL/INTERP/*.so
%dir %{perl_vendorarch}/auto/PDL/GSL/RNG
%{perl_vendorarch}/auto/PDL/GSL/RNG/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/GSL/RNG/*.so
%{_mandir}/man3/PDL::GSL::*

%files GSLSF
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/GSLSF
%dir %{perl_vendorarch}/auto/PDL/GSLSF
%dir %{perl_vendorarch}/auto/PDL/GSLSF/*
%{perl_vendorarch}/auto/PDL/GSLSF/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/GSLSF/*/*.so
%{_mandir}/man3/PDL::GSLSF::*

%files Demos
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::BAD*
%{perl_vendorarch}/PDL/Demos
