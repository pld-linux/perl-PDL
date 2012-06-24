# conditional build
#    with_html - generate an extra package with PDL documentation in HTML
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PDL
Summary:	perlDL - efficient numerical computing for Perl
Summary(pl):	perlDL - wydajne obliczenia numeryczne w Perlu
Summary(pt_BR):	M�dulo PDL para perl
Name:		perl-PDL
Version:	2.3.3
Release:	4
Epoch:		1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
Patch0:		%{name}-conf.patch
Patch1:		%{name}-dep.patch
Patch2:		%{name}-Makefile.PL.patch-dumb
Patch3:		%{name}-fftw-shared.patch
Patch4:		%{name}-WITH_IO_BROWSER.patch
URL:		http://pdl.perl.org/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	fftw-devel >= 2.1.3-5
BuildRequires:	gsl-devel >= 1.0
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-ExtUtils-F77 >= 1.10
BuildRequires:	perl-Filter
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	perl-PGPLOT
BuildRequires:	perl-Tk
BuildRequires:	rpm-perlprov >= 3.0.3-18
Provides:	perl(PDL::Lite)
Provides:	perl(PDL::LiteF)
Provides:	perl(PDL::PP::CType)
Provides:	perl(PDL::PP::Dims)
Provides:	perl(PDL::PP::PDLCode)
Provides:	perl(PDL::PP::SymTab)
Provides:	perl(PDL::PP::XS)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1
%define		_noautoreq	"perl(local.perldlrc)"

%description
The perlDL project aims to turn Perl into an efficient numerical
language for scientific computing. The PDL module gives standard Perl
the ability to COMPACTLY store and SPEEDILY manipulate the large
N-dimensional data sets which are the bread and butter of scientific
computing, i.e. C<$a=$b+$c> can add two 2048x2048 images in only a
fraction of a second.

%description -l pl
Modu� perlDL rozszerza mo�liwo�ci Perla o funkcje do oblicze�
numerycznych. Umo�liwia przechowywanie oraz szybkie manipulowanie
du�ymi n-wymiarowymi zbiorami danych, kt�re s� chlebem powszednim
naukowych oblicze�, np.: C<$a=$b+$c> dodaje dwie bitmapy rozmiaru
2048x2048 w u�amku sekundy.

%description -l pt_BR
O projeto perlDL pretende tornar perl uma linguagem n�merica eficiente
para computa��o cient�fica. O m�dulo PDL d� ao perl a habilidade de
armazenar de forma compacta e manipular rapidamente grandes conjuntos
de dados de N dimens�es que s�o muito comuns em computa��o cient�fica.
Ex. $a=$b+$c pode adicionar imagens de 2048x2048 em apenas uma fra��o
de segundo.

%package perldl
Summary:	PDL shell
Summary(pl):	Pow�oka PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description perldl
The program perldl is a simple shell (written in perl) for interactive
use of PDL. perl/PDL commands can simply be typed in - and edited if
you have appropriate version of the ReadLines and ReadKeys modules
installed. In that case perldl also supports a history mechanism.

%description perldl -l pl
Program perldl jest prost� pow�ok� napisan� w Perlu do interaktywnego
wykonywania funkcji modu�u PDL. Komendy Perla lub PDL mog� by� w
prosty spos�b wprowadzane, a tak�e edytowane je�li masz zainstalowan�
odpowiedni� wersj� modu�� ReadLines oraz ReadKeys. W tym ostatnim
przypadku perldl wspiera mechanizm historii komend.

%package Graphics-TriD
Summary:	PDL 3D interface
Summary(pl):	Interfejs 3D dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
Requires:	%{name}-Graphics-OpenGL = %{version}
Requires:	%{name}-IO-Pic = %{version}
Provides:	perl(PDL::Graphics::TriD::GL)
Provides:	perl(PDL::Graphics::TriD::Objects)
Provides:	perl(PDL::Graphics::TriD::TextObjects)

%description Graphics-TriD
This module implements a generic 3D plotting interface for PDL.
Points, lines and surfaces (among other objects) are supported.

With OpenGL, it is easy to manipulate the resulting 3D objects with
the mouse in real time - this helps data visualization a lot.

With VRML, you can generate objects for everyone to see with e.g.
Silicon Graphics' Cosmo Player. You can find out more about VRML at
`http://vrml.sgi.com/' or `http://www.vrml.org/'

%description Graphics-TriD -l pl
Modu� ten implementuje podstawowy interfejs 3D dla PDL. Dost�pne s� -
w�r�d innych obiekt�w - punkty, linie oraz powierzchnie.

Za pomoc� OpenGL, stworzonymi obiektami 3D mo�na �atwo manipulowa� w
czasie rzeczywistym za pomoc� myszy, co bardzo wspomaga wizualizacj�
danych.

Mo�esz te� generowa� obiekty w formacie VRML, kt�re mog� by� ogl�dane
przez inne osoby za pomoc� np.: programu Cosmo Player firmy Silicon
Graphics. Wi�cej na temat VRML mo�esz znale�� pod adresami
http://vrml.sgi.com/ lub http://www.vrml.org/.

%package Graphics-TriD-Tk
Summary:	A Tk widget interface to the PDL-Graphics-TriD
Summary(pl):	Kontrolka interfejsu Tk dla PDL-Graphics-TriD
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
Requires:	%{name}-Graphics-OpenGL = %{version}
Requires:	%{name}-Graphics-TriD = %{version}

%description Graphics-TriD-Tk
The widget is composed of a Frame and the Display device of the TriD
output. It inherits all of the attributes of a Tk Frame. All of the
events associated with this window are handled through Tk with the
exception of the <expose> event which must be handled by TriD because
the Frame is never exposed. Default mouse bindings, defined for
button1 and button3, control TriD object orientation and size
respectively.

%description Graphics-TriD-Tk -l pl
Kontrolka ta sk�ada si� z obiektu Frame oraz urz�dzenia Display modu�u
TriD. Dziedziczy ona wszystkie atrybuty obiektu Tk Frame. Wszystkie
zdarzenia skojarzone z tym oknem kontrolki s� obs�ugiwane za pomoc� Tk
za wyj�tkiem zdarzenia <expose>, kt�re musi by� obs�u�one przez modu�
TriD, poniewa� obiekt Frame nie jest nigdy wy�wietlany. Za pomoc�
przycisk�w myszki mo�na kontrolowa� widok obiektu (przycisk pierwszy)
oraz jego rozmiar (przycisk trzeci).

%package docs
Summary:	Supplied extra documentation for PDL::* perl modules.
Summary(pl):	Dodatkowo dostarczona dokumentacja do modu��w perla PDL::*.
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description docs
Additional, supplied by authors, documentation to all PDL::* modules.

%description docs -l pl
Dodatkowa, dostarczona przez autor�w, dokumentacja do modu��w PDL::*.

%if %{!?_with_html:0}%{?_with_html:1}
%package docs-HTML
Summary:	Supplied extra documentation for PDL::* perl modules in HTML format.
Summary(pl):	Dodatkowo dostarczona dokumentacja w HTML-u do modu��w perla PDL::*.
Group:		Development/Languages/Perl
# for install dir
Requires:	%{name}

%description docs-HTML
Additional, supplied by authors, documentation in HTML format to all
PDL::* modules.

%description docs-HTML -l pl
Dodatkowa, dostarczona przez autor�w, dokumentacja do modu��w PDL::*,
w formacie HTML.
%endif

%package Graphics-PGPLOT
Summary:	PGPLOT enhanced interface for PDL
Summary(pl):	Rozszerzony interfejs biblioteki PGPLOT dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Graphics-PGPLOT
`PDL::Graphics::PGPLOT' is a convenience interface to the PGPLOT
commands, implemented using the object oriented PGPLOT plotting
package in the PDL::Graphics::PGPLOT::Window manpage. See the
documentation for that package for in-depth information about the
usage of these commands and the options they accept.

%description Graphics-PGPLOT -l pl
Modu� ten jest interfejsem do komend biblioteki PGPLOT. Jest ona
zaimplementowany za pomoc� obiektowo zorientowanego pakietu PGPLOT
(sp�jrz do manuala modu�u PDL::Graphics::PGPLOT::Window).

%package Graphics-IIS
Summary:	Display PDL images on IIS devices (saoimage/ximtool)
Summary(pl):	Wy�wietlanie grafiki PDL na urz�dzeniach IIS (saoimage/ximtool)
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Graphics-IIS
Display PDL images on IIS devices (saoimage/ximtool).

%description Graphics-IIS -l pl
Wy�wietlanie grafiki PDL na urz�dzeniach IIS (saoimage/ximtool).

%package Graphics-LUT
Summary:	Provides access to a number of look-up tables for PDL
Summary(pl):	Dost�p do tablic kolor�w dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Graphics-LUT
Provides access to a number of look-up tables for PDL.

%description Graphics-LUT -l pl
Modu� zapewnia dost�p do r�nych tablic kolor�w (palet) dla PDL.

%package Graphics-OpenGL
Summary:	PDL interface to the OpenGL graphics library
Summary(pl):	Interfejs OpenGL dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Graphics-OpenGL
PDL interface to the OpenGL graphics library.

%description Graphics-OpenGL -l pl
Interfejs OpenGL dla PDL.

%package IO-Browser
Summary:	2D data browser for PDL
Summary(pl):	Przegl�darka danych 2D dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description IO-Browser
2D data browser for PDL.

%description -l pl IO-Browser
Przegl�darka danych 2D dla PDL.

%package IO-FastRaw
Summary:	A simple, fast and convenient IO format for PDL
Summary(pl):	Prosty, szybki i wygodny format wej�cia/wyj�cia dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description IO-FastRaw
A simple, fast and convenient IO format for PDL.

%description IO-FastRaw -l pl
Prosty, szybki i wygodny format wej�cia/wyj�cia dla PDL.

%package IO-FlexRaw
Summary:	A flexible binary IO format for PDL
Summary(pl):	Elastyczny binarny format wej�cia/wyj�cia dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description IO-FlexRaw
A flexible binary IO format for PDL.

%description IO-FlexRaw -l pl
Elastyczny binarny format wej�cia/wyj�cia dla PDL.

%package IO-NDF
Summary:	Starlink N-dimensional data structures for PDL
Summary(pl):	Wsparcie dla n-wymiarowych struktur danych firmy Starlink dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description IO-NDF
Starlink N-dimensional data structures for PDL.

%description IO-NDF -l pl
Wsparcie dla n-wymiarowych struktur danych firmy Starlink dla PDL.

%package IO-Pic
Summary:	Image I/O for PDL based on the netpbm package
Summary(pl):	Obs�uga obrazk�w dla PDL oparta na pakiecie netpbm
Group:		Development/Languages/Perl
Requires:	netpbm
Requires:	%{name} = %{version}
Requires:	%{name}-IO-Pnm = %{version}

%description IO-Pic
This package implements I/O for a number of popular image formats by
exploiting the xxxtopnm and pnmtoxxx converters from the netpbm
package.

%description IO-Pic -l pl
Pakiet daje mo�liwo�� czytania i zapisywania obrazk�w w wielu
formatach poprzez wykorzystywanie konwerter�w xxxtopnm i pnmtoxxx z
pakietu netpbm.

%package IO-Pnm
Summary:	PNM format IO for PDL
Summary(pl):	Wsparcie dla formatu PNM dla PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description IO-Pnm
PNM format IO for PDL.

%description IO-Pnm -l pl
Wsparcie dla formatu PNM dla PDL.

%package Slatec
Summary:	PDL interface to the Slatec numerical programming library
Summary(pl):	Interfejs PDL do biblioteki numerycznej Slatec
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Slatec
PDL interface to the Slatec numerical programming library.

%description Slatec -l pl
Interfejs PDL do biblioteki numerycznej Slatec.

%package GSL
Summary:	PDL interface to RNG and randist routines in GSL
Summary(pl):	Interfejs PDL do funkcji RNG i randist z biblioteki GSL
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description GSL
Interface to the rng and randist packages present in the GNU
Scientific Library.

%description GSL -l pl
Interfejs do funkcji rng i randist z biblioteki GSL.

%package Demos
Summary:	PDL demos
Summary(pl):	Przyk�adowe skrypty z u�yciem PDL
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
Requires:	%{name}-Graphics-LUT = %{version}
Requires:	%{name}-Graphics-PGPLOT = %{version}
Requires:	%{name}-Graphics-TriD = %{version}
Requires:	%{name}-Graphics-TriD-Tk = %{version}
Provides:	perl(PDL::Demos::Screen)

%description Demos
PDL demos.

%description Demos -l pl
Przyk�adowe skrypty z u�yciem PDL.

%prep
%setup -q -n %{pdir}-%{version}
%patch0 -p1 
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# g77 flags for compiling Slatec:
perl -pi -e 's@o \$mycflags s@o %{rpmcflags} s@' Lib/Slatec/Makefile.PL

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags} \
	-I%{_includedir}/ncurses -DNCURSES -DPERL_POLLUTE" 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# perl script to regenerate pdldoc database
install Doc/scantree.pl $RPM_BUILD_ROOT%{perl_sitearch}/PDL/scantree.pl

# some manuals have wrong names - this can be fixed in "Makefile.PL"s or here:
cd $RPM_BUILD_ROOT%{_mandir}/man3
mv -f PDL::Dev.3pm		PDL::Core::Dev.3pm
mv -f PDL::Linear.3pm		PDL::Filter::Linear.3pm
mv -f PDL::LinPred.3pm		PDL::Filter::LinPred.3pm
mv -f PDL::LM.3pm		PDL::Fit::LM.3pm
mv -f PDL::Linfit.3pm 		PDL::Fit::Linfit.3pm
mv -f PDL::Polynomial.3pm	PDL::Fit::Polynomial.3pm
mv -f PDL::State.3pm		PDL::Graphics::State.3pm
mv -f PDL::Histogram.3pm	PDL::RandVar::Histogram.3pm
mv -f PDL::Sobol.3pm		PDL::RandVar::Sobol.3pm

# some man pages do not belong to the man1 section
cd $RPM_BUILD_ROOT%{_mandir}/man1
for i in PDL::*.1; do
	mv $i ../man3/`echo $i | sed 's/\.1$/.3/'`
done

%clean
rm -rf $RPM_BUILD_ROOT

%post docs
/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}

%post Graphics-TriD
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%post Graphics-TriD-Tk
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%post Graphics-PGPLOT
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%post Graphics-IIS
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%post Graphics-LUT
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%post Graphics-OpenGL
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%post IO-Browser
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%post IO-FastRaw
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%post IO-FlexRaw
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%post IO-NDF
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%post IO-Pic
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%post IO-Pnm
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%post Slatec
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%post GSL
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%post Demos
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%postun Graphics-TriD
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%postun Graphics-TriD-Tk
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%postun Graphics-PGPLOT
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%postun Graphics-IIS
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%postun Graphics-LUT
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%postun Graphics-OpenGL
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%postun IO-Browser
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%postun IO-FastRaw
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%postun IO-FlexRaw
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%postun IO-NDF
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%postun IO-Pic
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%postun IO-Pnm
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%postun Slatec
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%postun GSL
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%postun Demos
if [ -f %{perl_sitearch}/PDL/scantree.pl ]; then
	/usr/bin/perl %{perl_sitearch}/PDL/scantree.pl %{perl_sitearch}
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pptemplate
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
%{perl_sitearch}/PDL/DiskCache.pm
%{perl_sitearch}/PDL/Doc
%{perl_sitearch}/PDL/Doc.pm
%{perl_sitearch}/PDL/Exporter.pm
%{perl_sitearch}/PDL/FFT.pm
%{perl_sitearch}/PDL/FFTW.pm
%dir %{perl_sitearch}/PDL/Filter
%{perl_sitearch}/PDL/Filter/Linear.pm
%dir %{perl_sitearch}/PDL/Fit
%{perl_sitearch}/PDL/Fit/Gaussian.pm
%{perl_sitearch}/PDL/Func.pm
%dir %{perl_sitearch}/PDL/Graphics
%{perl_sitearch}/PDL/Graphics/State.pm
%{perl_sitearch}/PDL/Image2D.pm
%{perl_sitearch}/PDL/ImageND.pm
%{perl_sitearch}/PDL/ImageRGB.pm
%dir %{perl_sitearch}/PDL/IO
%{perl_sitearch}/PDL/IO/Dumper.pm
%{perl_sitearch}/PDL/IO/Misc.pm
%{perl_sitearch}/PDL/LiteF.pm
%{perl_sitearch}/PDL/Lite.pm
%{perl_sitearch}/PDL/Lvalue.pm
%{perl_sitearch}/PDL/Math.pm
%{perl_sitearch}/PDL/NiceSlice.pm
%{perl_sitearch}/PDL/Opt
%{perl_sitearch}/PDL/Ops.pm
%{perl_sitearch}/PDL/Options.pm
%{perl_sitearch}/PDL/PP
%{perl_sitearch}/PDL/PP.pm
%{perl_sitearch}/PDL/Primitive.pm
%{perl_sitearch}/PDL/Pod
%{perl_sitearch}/PDL/RandVar.pm
%{perl_sitearch}/PDL/RandVar
%{perl_sitearch}/PDL/Reduce.pm
%{perl_sitearch}/PDL/Slices.pm
%{perl_sitearch}/PDL/Tests.pm
%{perl_sitearch}/PDL/Types.pm
%{perl_sitearch}/PDL/Ufunc.pm
%{perl_sitearch}/PDL/Version.pm
%{perl_sitearch}/PDL/default.perldlrc

%dir %{perl_sitearch}/auto/PDL
%dir %{perl_sitearch}/auto/PDL/Bad
%{perl_sitearch}/auto/PDL/Bad/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Bad/*.so
%dir %{perl_sitearch}/auto/PDL/Complex
%{perl_sitearch}/auto/PDL/Complex/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Complex/*.so
%dir %{perl_sitearch}/auto/PDL/FFT
%{perl_sitearch}/auto/PDL/FFT/*bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/FFT/*so
%dir %{perl_sitearch}/auto/PDL/FFTW
%{perl_sitearch}/auto/PDL/FFTW/*bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/FFTW/*so
%dir %{perl_sitearch}/auto/PDL/Graphics
%dir %{perl_sitearch}/auto/PDL/IO

%dir %{perl_sitearch}/auto/PDL/Image2D
%{perl_sitearch}/auto/PDL/Image2D/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Image2D/*.so
%dir %{perl_sitearch}/auto/PDL/ImageRGB
%{perl_sitearch}/auto/PDL/ImageRGB/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/ImageRGB/*.so
%dir %{perl_sitearch}/auto/PDL/Ops
%{perl_sitearch}/auto/PDL/Ops/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Ops/*.so
%dir %{perl_sitearch}/auto/PDL/Slices
%{perl_sitearch}/auto/PDL/Slices/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Slices/*.so
%dir %{perl_sitearch}/auto/PDL/Ufunc
%{perl_sitearch}/auto/PDL/Ufunc/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Ufunc/*.so
%dir %{perl_sitearch}/auto/PDL/CallExt
%{perl_sitearch}/auto/PDL/CallExt/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/CallExt/*.so
%dir %{perl_sitearch}/auto/PDL/Core
%{perl_sitearch}/auto/PDL/Core/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Core/*.so
%dir %{perl_sitearch}/auto/PDL/Fit
%dir %{perl_sitearch}/auto/PDL/Fit/Gaussian
%{perl_sitearch}/auto/PDL/Fit/Gaussian/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Fit/Gaussian/*.so
%dir %{perl_sitearch}/auto/PDL/ImageND
%{perl_sitearch}/auto/PDL/ImageND/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/ImageND/*.so
%dir %{perl_sitearch}/auto/PDL/IO/Misc
%{perl_sitearch}/auto/PDL/IO/Misc/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/IO/Misc/*.so
%dir %{perl_sitearch}/auto/PDL/Math
%{perl_sitearch}/auto/PDL/Math/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Math/*.so
%dir %{perl_sitearch}/auto/PDL/Primitive
%{perl_sitearch}/auto/PDL/Primitive/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Primitive/*.so
%dir %{perl_sitearch}/auto/PDL/Tests
%{perl_sitearch}/auto/PDL/Tests/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Tests/*.so

%{perl_sitearch}/Inline/Pdlpp.pm

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
%{_mandir}/man3/PDL::Func.3pm.gz
%{_mandir}/man3/PDL::Graphics::State.3pm*
%{_mandir}/man3/PDL::I[mn]*
%{_mandir}/man3/PDL::IO::Misc*
%{_mandir}/man3/PDL::Math*
%{_mandir}/man3/PDL::NiceSlice.3pm*
%{_mandir}/man3/PDL::Slices*
%{_mandir}/man3/PDL::pptemplate.3pm*

%files docs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdldoc
%attr(755,root,root) %{perl_sitearch}/PDL/scantree.pl
%ghost %{perl_sitearch}/PDL/pdldoc.db
%doc %{perl_sitearch}/PDL/*.pod
%{_mandir}/man1/pdldoc.1*

%if %{!?_with_html:0}%{?_with_html:1}
%files docs-HTML
%doc %{perl_sitearch}/PDL/HtmlDocs
%endif

%files perldl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perldl
%{_mandir}/man1/perldl*

%files Graphics-TriD
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::Graphics::TriD.*
%{_mandir}/man3/PDL::Graphics::TriD::[A-SU-Z]*
%dir %{perl_sitearch}/auto/PDL/Graphics/TriD
%dir %{perl_sitearch}/auto/PDL/Graphics/TriD/Rout
%{perl_sitearch}/auto/PDL/Graphics/TriD/Rout/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Graphics/TriD/Rout/*.so
%dir %{perl_sitearch}/PDL/Graphics/TriD
%{perl_sitearch}/PDL/Graphics/TriD/[A-SU-Z]*
%{perl_sitearch}/PDL/Graphics/TriD/Te*
%{perl_sitearch}/PDL/Graphics/VRML*
%{perl_sitearch}/PDL/Graphics/TriD.pm

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
%{perl_sitearch}/auto/PDL/Graphics/PGPLOT/Window/*.bs
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
%{perl_sitearch}/auto/PDL/Graphics/IIS/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Graphics/IIS/*.so
%{perl_sitearch}/PDL/Graphics/IIS*

%files Graphics-OpenGL
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::Graphics::OpenGL*
%dir %{perl_sitearch}/auto/PDL/Graphics/OpenGL*
%{perl_sitearch}/auto/PDL/Graphics/OpenGL*/*bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Graphics/OpenGL*/*so
%{perl_sitearch}/PDL/Graphics/OpenGL*

%files IO-Browser
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::IO::Browser*
%dir %{perl_sitearch}/auto/PDL/IO/Browser
%{perl_sitearch}/auto/PDL/IO/Browser/*.bs
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
%{perl_sitearch}/auto/PDL/IO/Pnm/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/IO/Pnm/*.so
%{perl_sitearch}/PDL/IO/Pnm*

%files Slatec
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::Filter::LinPred*
%{_mandir}/man3/PDL::Fit::Linfit*
%{_mandir}/man3/PDL::Fit::LM*
%{_mandir}/man3/PDL::Fit::Polynomial*
%{_mandir}/man3/PDL::Gaussian*
%{_mandir}/man3/PDL::Matrix*
%{_mandir}/man3/PDL::Slatec*
%{perl_sitearch}/PDL/Filter/LinPred.pm
%{perl_sitearch}/PDL/Fit/Linfit.pm
%{perl_sitearch}/PDL/Fit/LM.pm
%{perl_sitearch}/PDL/Fit/Polynomial.pm
%{perl_sitearch}/PDL/Gaussian.pm
%{perl_sitearch}/PDL/Matrix.pm
%{perl_sitearch}/PDL/Slatec.pm
%dir %{perl_sitearch}/auto/PDL/Slatec
%{perl_sitearch}/auto/PDL/Slatec/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/Slatec/*.so

%files GSL
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::GSL*
%{perl_sitearch}/PDL/GSL
%dir %{perl_sitearch}/auto/PDL/GSL
%dir %{perl_sitearch}/auto/PDL/GSL/RNG
%{perl_sitearch}/auto/PDL/GSL/RNG/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/PDL/GSL/RNG/*.so

%files Demos
%defattr(644,root,root,755)
%{_mandir}/man3/PDL::BAD*
%{perl_sitearch}/PDL/Demos
