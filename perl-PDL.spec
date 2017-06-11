#
# Conditional build:
%bcond_with	html	# generate package with PDL documentation in HTML
%bcond_with	tests	# perform "make test"
			# require a valid DISPLAY
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PDL
Summary:	perlDL - efficient numerical computing for Perl
Summary(pl.UTF-8):	perlDL - wydajne obliczenia numeryczne w Perlu
Summary(pt_BR.UTF-8):	Módulo PDL para perl
Name:		perl-PDL
Version:	2.015
Release:	4
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://downloads.sourceforge.net/pdl/%{pdir}-%{version}.tar.gz
# Source0-md5:	fe2da41811efce2fdf874c64842c6a43
Patch0:		%{name}-conf.patch
Patch1:		%{name}-dep.patch
Patch2:		%{name}-Makefile.PL.patch-dumb
Patch4:		%{name}-vendorarch.patch
Patch5:		PDL-Disable-PDL-GIS-Proj.patch
Patch7:		%{name}-gsl.patch
URL:		http://pdl.perl.org/
BuildRequires:	gd-devel
BuildRequires:	gsl-devel >= 1.3
BuildRequires:	libgfortran-static
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	perl-Devel-CheckLib
BuildRequires:	perl-ExtUtils-F77 >= 1.10
BuildRequires:	perl-Filter
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	perl-OpenGL >= 0.6702
BuildRequires:	perl-PGPLOT
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-perldoc
BuildRequires:	proj-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1
%define		_noautoreq_perl	local.perldlrc PDL::Graphics::TriD::GObject

%description
The perlDL project aims to turn Perl into an efficient numerical
language for scientific computing. The PDL module gives standard Perl
the ability to COMPACTLY store and SPEEDILY manipulate the large
N-dimensional data sets which are the bread and butter of scientific
computing, i.e. $a=$b+$c can add two 2048x2048 images in only a
fraction of a second.

%description -l pl.UTF-8
Moduł perlDL rozszerza możliwości Perla o funkcje do obliczeń
numerycznych. Umożliwia przechowywanie oraz szybkie manipulowanie
dużymi n-wymiarowymi zbiorami danych, które są chlebem powszednim
naukowych obliczeń, np.: $a=$b+$c dodaje dwie bitmapy rozmiaru
2048x2048 w ułamku sekundy.

%description -l pt_BR.UTF-8
O projeto perlDL pretende tornar perl uma linguagem númerica eficiente
para computação científica. O módulo PDL dá ao perl a habilidade de
armazenar de forma compacta e manipular rapidamente grandes conjuntos
de dados de N dimensões que são muito comuns em computação científica.
Ex. $a=$b+$c pode adicionar imagens de 2048x2048 em apenas uma fração
de segundo.

%package perldl
Summary:	PDL shell
Summary(pl.UTF-8):	Powłoka PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description perldl
The program perldl is a simple shell (written in perl) for interactive
use of PDL. perl/PDL commands can simply be typed in - and edited if
you have appropriate version of the ReadLines and ReadKeys modules
installed. In that case perldl also supports a history mechanism.

%description perldl -l pl.UTF-8
Program perldl jest prostą powłoką napisaną w Perlu do interaktywnego
wykonywania funkcji modułu PDL. Komendy Perla lub PDL mogą być w
prosty sposób wprowadzane, a także modyfikowane jeśli zainstalowane
są odpowiednie wersje modułów ReadLines oraz ReadKeys. W tym ostatnim
przypadku perldl obsługuje mechanizm historii komend.

%package perldl2
Summary:	New and improved PDL shell
Summary(pl.UTF-8):	Nowa i usprawniona powłoka PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description perldl2
The program perldl2 is a simple shell (written in perl) for interactive
use of PDL. perl/PDL commands can simply be typed in - and edited if
you have appropriate version of the ReadLines and ReadKeys modules
installed. In that case perldl2 also supports a history mechanism.

%description perldl2 -l pl.UTF-8
Program perldl2 jest prostą powłoką napisaną w Perlu do interaktywnego
wykonywania funkcji modułu PDL. Komendy Perla lub PDL mogą być w
prosty sposób wprowadzane, a także modyfikowane jeśli zainstalowane
są odpowiednie wersje modułów ReadLines oraz ReadKeys. W tym ostatnim
przypadku perldl2 obsługuje mechanizm historii komend.

%package docs
Summary:	Supplied extra documentation for PDL::* perl modules
Summary(pl.UTF-8):	Dodatkowo dostarczona dokumentacja do modułów perla PDL::*
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description docs
Additional, supplied by authors, documentation to all PDL::* modules.

%description docs -l pl.UTF-8
Dodatkowa, dostarczona przez autorów, dokumentacja do modułów PDL::*.

%package docs-HTML
Summary:	Supplied extra documentation for PDL::* perl modules in HTML format
Summary(pl.UTF-8):	Dodatkowo dostarczona dokumentacja w HTML-u do modułów perla PDL::*
Group:		Development/Languages/Perl
# for install dir
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description docs-HTML
Additional, supplied by authors, documentation in HTML format to all
PDL::* modules.

%description docs-HTML -l pl.UTF-8
Dodatkowa, dostarczona przez autorów, dokumentacja do modułów PDL::*,
w formacie HTML.

%package Graphics-IIS
Summary:	Display PDL images on IIS devices (saoimage/ximtool)
Summary(pl.UTF-8):	Wyświetlanie grafiki PDL na urządzeniach IIS (saoimage/ximtool)
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Graphics-IIS
Display PDL images on IIS devices (saoimage/ximtool).

%description Graphics-IIS -l pl.UTF-8
Wyświetlanie grafiki PDL na urządzeniach IIS (saoimage/ximtool).

%package Graphics-LUT
Summary:	Provides access to a number of look-up tables for PDL
Summary(pl.UTF-8):	Dostęp do tablic kolorów dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Graphics-LUT
Provides access to a number of look-up tables for PDL.

%description Graphics-LUT -l pl.UTF-8
Moduł zapewnia dostęp do różnych tablic kolorów (palet) dla PDL.

%package Graphics-Limits
Summary:	Derive limits for display purposes
Summary(pl.UTF-8):	Oblicza zakresy dla danych w celu wizualizacji
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Graphics-Limits
Functions to derive limits for data for display purposes.

%description Graphics-Limits -l pl.UTF-8
Funkcje obliczające zakresy dla danych w celu wizualizacji.

%package Graphics-OpenGL
Summary:	PDL interface to the OpenGL graphics library
Summary(pl.UTF-8):	Interfejs OpenGL dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Graphics-OpenGL
PDL interface to the OpenGL graphics library.

%description Graphics-OpenGL -l pl.UTF-8
Interfejs OpenGL dla PDL.

%package Graphics-PGPLOT
Summary:	PGPLOT enhanced interface for PDL
Summary(pl.UTF-8):	Rozszerzony interfejs biblioteki PGPLOT dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Graphics-PGPLOT
`PDL::Graphics::PGPLOT' is a convenience interface to the PGPLOT
commands, implemented using the object oriented PGPLOT plotting
package in the PDL::Graphics::PGPLOT::Window manpage. See the
documentation for that package for in-depth information about the
usage of these commands and the options they accept.

%description Graphics-PGPLOT -l pl.UTF-8
Moduł ten jest interfejsem do komend biblioteki PGPLOT. Jest ona
zaimplementowany za pomocą obiektowo zorientowanego pakietu PGPLOT
(spójrz do manuala modułu PDL::Graphics::PGPLOT::Window).

%package Graphics-TriD
Summary:	PDL 3D interface
Summary(pl.UTF-8):	Interfejs 3D dla PDL
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

%description Graphics-TriD -l pl.UTF-8
Moduł ten implementuje podstawowy interfejs 3D dla PDL. Dostępne są -
wśród innych obiektów - punkty, linie oraz powierzchnie.

Za pomocą OpenGL, stworzonymi obiektami 3D można łatwo manipulować w
czasie rzeczywistym za pomocą myszy, co bardzo wspomaga wizualizację
danych.

Możesz też generować obiekty w formacie VRML, które mogą być oglądane
przez inne osoby za pomocą np.: programu Cosmo Player firmy Silicon
Graphics. Więcej na temat VRML możesz znaleźć pod adresami
http://vrml.sgi.com/ lub http://www.vrml.org/.

%package IO-Browser
Summary:	2D data browser for PDL
Summary(pl.UTF-8):	Przeglądarka danych 2D dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description IO-Browser
2D data browser for PDL.

%description IO-Browser -l pl.UTF-8
Przeglądarka danych 2D dla PDL.

%package IO-Dicom
Summary:	Module for reading DICOM images
Summary(pl.UTF-8):	Moduł służący do czytania obrazów w formacie DICOM
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description IO-Dicom
The PDL::IO::Dicom module enables reading 16-bit gray level Dicom
images into PDL. As Dicom is an extremely complex format, this module
can unfortunately not handle all different image types included in the
DICOM standard. One common format that is currently not supported is
the Papyrus format.

%description IO-Dicom -l pl.UTF-8
Moduł PDL::IO::Dicom umożliwia czytanie obrazów w 16-bitowej skali
szarości w formacie DICOM. Ponieważ DICOM jest niezwykle
skomplikowanym formatem, ten moduł nie jest w stanie przeczytać
wszystkich rodzajów obrazów zdefiniowanych w standardzie DICOM.
Np. format Papyrus jest obecnie nie obsługiwany.

%package IO-FastRaw
Summary:	A simple, fast and convenient IO format for PDL
Summary(pl.UTF-8):	Prosty, szybki i wygodny format wejścia/wyjścia dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description IO-FastRaw
A simple, fast and convenient IO format for PDL.

%description IO-FastRaw -l pl.UTF-8
Prosty, szybki i wygodny format wejścia/wyjścia dla PDL.

%package IO-FlexRaw
Summary:	A flexible binary IO format for PDL
Summary(pl.UTF-8):	Elastyczny binarny format wejścia/wyjścia dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description IO-FlexRaw
A flexible binary IO format for PDL.

%description IO-FlexRaw -l pl.UTF-8
Elastyczny binarny format wejścia/wyjścia dla PDL.

%package IO-GD
Summary:	PDL interface to the GD c library
Summary(pl.UTF-8):	Interfejs PLD do biblioteki GD
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description IO-GD
PDL interface to the GD c library.

%description IO-GD -l pl.UTF-8
Interfejs PLD do biblioteki GD.

%package IO-Pic
Summary:	Image I/O for PDL based on the netpbm package
Summary(pl.UTF-8):	Obsługa obrazków dla PDL oparta na pakiecie netpbm
Group:		Development/Languages/Perl
Requires:	netpbm
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-IO-Pnm = %{epoch}:%{version}-%{release}

%description IO-Pic
This package implements I/O for a number of popular image formats by
exploiting the xxxtopnm and pnmtoxxx converters from the netpbm
package.

%description IO-Pic -l pl.UTF-8
Pakiet daje możliwość czytania i zapisywania obrazków w wielu
formatach poprzez wykorzystywanie konwerterów xxxtopnm i pnmtoxxx z
pakietu netpbm.

%package IO-Pnm
Summary:	PNM format IO for PDL
Summary(pl.UTF-8):	Wsparcie dla formatu PNM dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description IO-Pnm
PNM format IO for PDL.

%description IO-Pnm -l pl.UTF-8
Wsparcie dla formatu PNM dla PDL.

%package IO-Storable
Summary:	Helper functions to make PDL usable with Storable
Summary(pl.UTF-8):	Funkcje pomocnicze pozwalajace używać PDL ze Storable
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description IO-Storable
Helper functions to make PDL usable with Storable.

%description IO-Storable -l pl.UTF-8
Funkcje pomocnicze pozwalajace używać PDL wraz ze Storable.

%package Slatec
Summary:	PDL interface to the Slatec numerical programming library
Summary(pl.UTF-8):	Interfejs PDL do biblioteki numerycznej Slatec
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Slatec
PDL interface to the Slatec numerical programming library.

%description Slatec -l pl.UTF-8
Interfejs PDL do biblioteki numerycznej Slatec.

%package GSL
Summary:	PDL interface to RNG and randist routines in GSL
Summary(pl.UTF-8):	Interfejs PDL do funkcji RNG i randist z biblioteki GSL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description GSL
Interface to the rng and randist packages present in the GNU
Scientific Library.

%description GSL -l pl.UTF-8
Interfejs do funkcji rng i randist z biblioteki GSL.

%package GSLSF
Summary:	PDL interface to GSL Special Functions
Summary(pl.UTF-8):	Interfejs PDL do funkcji specjalnych GSL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description GSLSF
PDL interface to GSL Special Functions.

%description GSLSF -l pl.UTF-8
Interfejs PDL do funkcji specjalnych GSL.

%package Minuit
Summary:	PDL interface to the Minuit library
Summary(pl.UTF-8):	Interfejs PDL do biblioteki Minuit
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Minuit
This package implements an interface to the Minuit minimization
routines (part of the CERN Library,
http://wwwasdoc.web.cern.ch/wwwasdoc/minuit/minmain.html)

%description Minuit -l pl.UTF-8
Ten pakiet udostępnia interfejs do funkcji minimizujących Minuit
(http://wwwasdoc.web.cern.ch/wwwasdoc/minuit/minmain.html).

%package Transform
Summary:	Coordinate transforms, image warping, and N-D functions
Summary(pl.UTF-8):	Transformacje współrzędnych, warpowaie obrazów i funkcje N-D
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Transform
PDL::Transform is a convenient way to represent coordinate
transformations and resample images.  It embodies functions mapping
R^N -> R^M, both with and without inverses.  Provision exists for
parametrizing functions, and for composing them.  You can use this
part of the Transform object to keep track of arbitrary functions
mapping R^N -> R^M with or without inverses.

%description Transform -l pl.UTF-8
Transformacje współrzędnych, warpowaie obrazów i funkcje N-D

%package Demos
Summary:	PDL demos
Summary(pl.UTF-8):	Przykładowe skrypty z użyciem PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-Graphics-LUT = %{epoch}:%{version}-%{release}
Requires:	%{name}-Graphics-PGPLOT = %{epoch}:%{version}-%{release}
Requires:	%{name}-Graphics-TriD = %{epoch}:%{version}-%{release}

%description Demos
PDL demos.

%description Demos -l pl.UTF-8
Przykładowe skrypty z użyciem PDL.

%prep
%setup -q -n %{pdir}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1

# g77 flags for compiling Slatec:
%{__perl} -pi -e 's@\) \$mycflags s@\) %{rpmcflags} -fPIC s@' Lib/Slatec/Makefile.PL

%{__perl} -pi -e "s@(OPENGL_LIBS.*)'-L/usr/lib@\$1'-L/usr/%{_lib}@" perldl.conf

ln -s Basic PDL

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} -j1 \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags} -I/usr/include/ncurses -DNCURSES -DPERL_POLLUTE"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 pure_install \
	DESTDIR=$RPM_BUILD_ROOT

perl -Mblib Doc/scantree.pl $RPM_BUILD_ROOT%{perl_vendorarch}
perl -pi -e "s|$RPM_BUILD_ROOT/|/|g" $RPM_BUILD_ROOT%{perl_vendorarch}/PDL/pdldoc.db

# perl script to regenerate pdldoc database
install Doc/scantree.pl $RPM_BUILD_ROOT%{perl_vendorarch}/PDL/scantree.pl

# some manuals have wrong names - this can be fixed in "Makefile.PL"s or here:
cd $RPM_BUILD_ROOT%{_mandir}/man3
%{__mv} PDL::Dev.3pm		PDL::Core::Dev.3pm
%{__mv} PDL::Linear.3pm		PDL::Filter::Linear.3pm
%{__mv} PDL::LinPred.3pm	PDL::Filter::LinPred.3pm
%{__mv} PDL::LM.3pm		PDL::Fit::LM.3pm
%{__mv} PDL::Linfit.3pm 	PDL::Fit::Linfit.3pm
%{__mv} PDL::Polynomial.3pm	PDL::Fit::Polynomial.3pm
%{__mv} PDL::State.3pm		PDL::Graphics::State.3pm
%{__mv} Pdlpp.3pm		Inline::Pdlpp.3pm

# some man pages do not belong to the man1 section
cd $RPM_BUILD_ROOT%{_mandir}/man1
for i in PDL::*.1*; do
	%{__mv} $i ../man3/`echo $i | sed 's/\.1p\?$/.3/'`
done

# Remove demos fo rexternal packages
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/PDL/Demos/{Gnuplot_demo,Prima}.pm

%clean
rm -rf $RPM_BUILD_ROOT

%post docs
/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}

%post Graphics-IIS
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post Graphics-LUT
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post Graphics-Limits
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

%post Graphics-TriD
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post IO-Browser
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post IO-Dicom
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

%post IO-GD
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

%post Minuit
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%post Transform
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

%postun Graphics-LUT
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun Graphics-Limits
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

%postun Graphics-TriD
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun IO-Browser
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun IO-Dicom
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

%postun IO-GD
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

%postun Minuit
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun Transform
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%postun Demos
if [ -f %{perl_vendorarch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_vendorarch}/PDL/scantree.pl %{perl_vendorarch}
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdl
%attr(755,root,root) %{_bindir}/pptemplate
%dir %{perl_vendorarch}/PDL

%{perl_vendorarch}/PDL.pm
%{perl_vendorarch}/PDL/AutoLoader.pm
%{perl_vendorarch}/PDL/Bad.pm
%{perl_vendorarch}/PDL/Basic.pm
%{perl_vendorarch}/PDL/CallExt.pm
%{perl_vendorarch}/PDL/Char.pm
%{perl_vendorarch}/PDL/Complex.pm
%{perl_vendorarch}/PDL/Compression.pm
%{perl_vendorarch}/PDL/Config.pm
%{perl_vendorarch}/PDL/Constants.pm
%{perl_vendorarch}/PDL/Core
%{perl_vendorarch}/PDL/Core.pm
%{perl_vendorarch}/PDL/Dbg.pm
%{perl_vendorarch}/PDL/DiskCache.pm
%{perl_vendorarch}/PDL/Doc
%{perl_vendorarch}/PDL/Doc.pm
%{perl_vendorarch}/PDL/Exporter.pm
%{perl_vendorarch}/PDL/FFT.pm
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
%dir %{perl_vendorarch}/PDL/Install
%{perl_vendorarch}/PDL/Install/Files.pm
%dir %{perl_vendorarch}/PDL/IO
%{perl_vendorarch}/PDL/IO/Dumper.pm
%{perl_vendorarch}/PDL/IO/FITS.pm
%{perl_vendorarch}/PDL/IO/IDL.pm
%{perl_vendorarch}/PDL/IO/Misc.pm
%{perl_vendorarch}/PDL/LiteF.pm
%{perl_vendorarch}/PDL/Lite.pm
%{perl_vendorarch}/PDL/Lvalue.pm
%{perl_vendorarch}/PDL/Math.pm
%{perl_vendorarch}/PDL/MatrixOps.pm
%{perl_vendorarch}/PDL/NiceSlice.pm
%dir %{perl_vendorarch}/PDL/NiceSlice
%{perl_vendorarch}/PDL/NiceSlice/FilterSimple.pm
%{perl_vendorarch}/PDL/NiceSlice/FilterUtilCall.pm
%{perl_vendorarch}/PDL/NiceSlice/ModuleCompile.pm
%{perl_vendorarch}/PDL/Opt
%{perl_vendorarch}/PDL/Ops.pm
%{perl_vendorarch}/PDL/Options.pm
%{perl_vendorarch}/PDL/PP
%{perl_vendorarch}/PDL/PP.pm
%{perl_vendorarch}/PDL/Primitive.pm
%{perl_vendorarch}/PDL/Reduce.pm
%{perl_vendorarch}/PDL/Slices.pm
%{perl_vendorarch}/PDL/Types.pm
%{perl_vendorarch}/PDL/Ufunc.pm
%{perl_vendorarch}/PDL/Version.pm
%{perl_vendorarch}/PDL/default.perldlrc

%dir %{perl_vendorarch}/auto/PDL
%dir %{perl_vendorarch}/auto/PDL/Bad
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Bad/*.so
%dir %{perl_vendorarch}/auto/PDL/Complex
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Complex/*.so
%dir %{perl_vendorarch}/auto/PDL/Compression
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Compression/*.so
%dir %{perl_vendorarch}/auto/PDL/FFT
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/FFT/*so
%dir %{perl_vendorarch}/auto/PDL/Graphics
%dir %{perl_vendorarch}/auto/PDL/IO

%dir %{perl_vendorarch}/auto/PDL/Image2D
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Image2D/*.so
%dir %{perl_vendorarch}/auto/PDL/ImageRGB
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/ImageRGB/*.so
%dir %{perl_vendorarch}/auto/PDL/Ops
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Ops/*.so
%dir %{perl_vendorarch}/auto/PDL/Slices
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Slices/*.so
%dir %{perl_vendorarch}/auto/PDL/Ufunc
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Ufunc/*.so
%dir %{perl_vendorarch}/auto/PDL/CallExt
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/CallExt/*.so
%dir %{perl_vendorarch}/auto/PDL/Core
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Core/*.so
%dir %{perl_vendorarch}/auto/PDL/Fit
%dir %{perl_vendorarch}/auto/PDL/Fit/Gaussian
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Fit/Gaussian/*.so
%dir %{perl_vendorarch}/auto/PDL/ImageND
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/ImageND/*.so
%dir %{perl_vendorarch}/auto/PDL/IO/Misc
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/IO/Misc/*.so
%dir %{perl_vendorarch}/auto/PDL/Math
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Math/*.so
%dir %{perl_vendorarch}/auto/PDL/MatrixOps
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/MatrixOps/*.so
%dir %{perl_vendorarch}/auto/PDL/Primitive
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Primitive/*.so

%{perl_vendorarch}/Inline/MakePdlppInstallable.pm
%{perl_vendorarch}/Inline/Pdlpp.pm

%{_mandir}/man1/pptemplate.1*
%{_mandir}/man3/Inline::Pdlpp.3pm*
%{_mandir}/man3/PDL.*
%{_mandir}/man3/PDL::[AC-ELO-RTU]*
%{_mandir}/man3/PDL::Ba*
%{_mandir}/man3/PDL::Bugs.3*
%{_mandir}/man3/PDL::FAQ*
%{_mandir}/man3/PDL::FFT*
%{_mandir}/man3/PDL::Filter::Linear*
%{_mandir}/man3/PDL::Fit::Gaussian*
%{_mandir}/man3/PDL::Func.3pm*
%{_mandir}/man3/PDL::Graphics::State.3pm*
%{_mandir}/man3/PDL::IFiles.3pm*
%{_mandir}/man3/PDL::I[mn]*
%{_mandir}/man3/PDL::IO.3pm*
%{_mandir}/man3/PDL::IO::FITS.3pm*
%{_mandir}/man3/PDL::IO::IDL.3pm*
%{_mandir}/man3/PDL::IO::Misc*
%{_mandir}/man3/PDL::Math*
%{_mandir}/man3/PDL::MatrixOps.3pm*
%{_mandir}/man3/PDL::Modules.3*
%{_mandir}/man3/PDL::NiceSlice.3pm*
%{_mandir}/man3/PDL::Slices*
%{_mandir}/man3/PDL::pdl2.3pm*
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

%files perldl2
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdl2
%{perl_vendorarch}/PDL/Perldl2
%{_mandir}/man1/pdl2*

%files Graphics-IIS
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/Graphics/IIS*
%dir %{perl_vendorarch}/auto/PDL/Graphics/IIS
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Graphics/IIS/*.so
%{_mandir}/man3/PDL::Graphics::IIS*

%files Graphics-LUT
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/Graphics/LUT*
%{_mandir}/man3/PDL::Graphics::LUT*

%files Graphics-Limits
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/Graphics/Limits*
%{_mandir}/man3/PDL::Graphics::Limits*

%files Graphics-OpenGL
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/Graphics/OpenGL*
%dir %{perl_vendorarch}/auto/PDL/Graphics/OpenGL*
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Graphics/OpenGL*/*so
%{_mandir}/man3/PDL::Graphics::OpenGL*

%files Graphics-PGPLOT
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/Graphics/PGPLOT*
%{perl_vendorarch}/PDL/Graphics2D*
%dir %{perl_vendorarch}/auto/PDL/Graphics/PGPLOT
%dir %{perl_vendorarch}/auto/PDL/Graphics/PGPLOT/Window
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Graphics/PGPLOT/Window/*.so
%{_mandir}/man3/PDL::Graphics2D*
%{_mandir}/man3/PDL::Graphics::PGPLOT*

%files Graphics-TriD
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/PDL/Graphics/TriD
%{perl_vendorarch}/PDL/Graphics/TriD/[A-SU-Z]*
%{perl_vendorarch}/PDL/Graphics/TriD/Te*
%{perl_vendorarch}/PDL/Graphics/VRML*
%{perl_vendorarch}/PDL/Graphics/TriD.pm
%dir %{perl_vendorarch}/auto/PDL/Graphics/TriD
%dir %{perl_vendorarch}/auto/PDL/Graphics/TriD/Rout
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Graphics/TriD/Rout/*.so
%{_mandir}/man3/PDL::Graphics::TriD.*
%{_mandir}/man3/PDL::Graphics::TriD::[A-SU-Z]*

%files IO-Browser
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::Browser*
%dir %{perl_vendorarch}/auto/PDL/IO/Browser
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/IO/Browser/*.so
%{perl_vendorarch}/PDL/IO/Browser*

%files IO-Dicom
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::Dicom*
%{perl_vendorarch}/PDL/IO/Dicom*

%files IO-FastRaw
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::FastRaw*
%{perl_vendorarch}/PDL/IO/FastRaw*

%files IO-FlexRaw
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::FlexRaw*
%{perl_vendorarch}/PDL/IO/FlexRaw*

%files IO-GD
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::GD*
%{perl_vendorarch}/PDL/IO/GD*
%dir %{perl_vendorarch}/auto/PDL/IO/GD
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/IO/GD/*.so

%files IO-Pic
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/IO/Pic*

%files IO-Pnm
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::Pnm*
%dir %{perl_vendorarch}/auto/PDL/IO/Pnm
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/IO/Pnm/*.so
%{perl_vendorarch}/PDL/IO/Pnm*

%files IO-Storable
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/IO/Storable.pm
%dir %{perl_vendorarch}/auto/PDL/IO/Storable
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/IO/Storable/*.so
%{_mandir}/man3/PDL::IO::Storable*

%files Slatec
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::Filter::LinPred*
%{_mandir}/man3/PDL::Fit::Linfit*
%{_mandir}/man3/PDL::Fit::LM*
%{_mandir}/man3/PDL::Fit::Polynomial*
%{_mandir}/man3/PDL::Matrix.3pm*
%{_mandir}/man3/PDL::Slatec*
%{perl_vendorarch}/PDL/Filter/LinPred.pm
%{perl_vendorarch}/PDL/Fit/Linfit.pm
%{perl_vendorarch}/PDL/Fit/LM.pm
%{perl_vendorarch}/PDL/Fit/Polynomial.pm
%{perl_vendorarch}/PDL/Matrix.pm
%{perl_vendorarch}/PDL/Slatec.pm
%dir %{perl_vendorarch}/auto/PDL/Slatec
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Slatec/*.so

%files GSL
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/GSL
%dir %{perl_vendorarch}/auto/PDL/GSL
%dir %{perl_vendorarch}/auto/PDL/GSL/DIFF
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/GSL/DIFF/*.so
%dir %{perl_vendorarch}/auto/PDL/GSL/INTEG
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/GSL/INTEG/*.so
%dir %{perl_vendorarch}/auto/PDL/GSL/INTERP
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/GSL/INTERP/*.so
%dir %{perl_vendorarch}/auto/PDL/GSL/MROOT
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/GSL/MROOT/*.so
%dir %{perl_vendorarch}/auto/PDL/GSL/RNG
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/GSL/RNG/*.so
%{_mandir}/man3/PDL::GSL::*

%files GSLSF
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/GSLSF
%dir %{perl_vendorarch}/auto/PDL/GSLSF
%dir %{perl_vendorarch}/auto/PDL/GSLSF/*
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/GSLSF/*/*.so
%{_mandir}/man3/PDL::GSLSF::*

%files Minuit
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/Minuit.pm
%dir %{perl_vendorarch}/auto/PDL/Minuit
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Minuit/*.so
%{_mandir}/man3/PDL::Minuit*

%files Transform
%defattr(644,root,root,755)
%{perl_vendorarch}/PDL/Transform.pm
%{perl_vendorarch}/PDL/Transform
%dir %{perl_vendorarch}/auto/PDL/Transform
%attr(755,root,root) %{perl_vendorarch}/auto/PDL/Transform/*.so

%files Demos
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::BAD*
%{perl_vendorarch}/PDL/Demos
