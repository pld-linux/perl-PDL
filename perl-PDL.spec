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
Group(pl):	Programowanie/J�zyki/Perl
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
perlDL rozsze�a mo�liwo�ci perl'a o funkcje do oblicze� numerycznych i
naukowaych.

%package perldl
Summary:	perlDL shell
Summary(pl):	Pow�oka perlDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl

%description perldl

%description -l pl perldl

%package Graphics-TriD
Summary:	perlDL OpenGL support
Summary(pl):	Wsparcie perlDL dla OpenGL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl

%description Graphics-TriD

%description -l pl Graphics-TriD

%package Graphics-TriD-Tk
Summary:	A Tk widget interface to the PDL-Graphics-TriD
Summary(pl):	Kontrolka interfejsu Tk dla PDL-Graphics-TriD
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl

%description Graphics-TriD-Tk

%description -l pl Graphics-TriD-Tk

%package Graphics-PGPLOT
Summary:	PGPLOT enhanced interface for PDL
Summary(pl):	Rozszerzony interfejs bibliotek PGPLOT dla PDL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl

%description Graphics-PGPLOT

%description -l pl Graphics-PGPLOT

%package Graphics-IIS
Summary:	Display PDL images on IIS devices (saoimage/ximtool)
Summary(pl):	Wy�wietlanie grafiki PDL na urz�dzeniach IIS (saoimage/ximtool)
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl

%description Graphics-IIS

%description -l pl Graphics-IIS

%package Graphics-OpenGL
Summary:	 Graphics-OpenGL
Summary(pl):	 Graphics-OpenGL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl

%description Graphics-OpenGL

%description -l pl Graphics-OpenGL

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
%{_mandir}/man3/*

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
%{perl_sitearch}/PDL/I*
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
%{perl_sitearch}/PDL/Graphics/LUT*
%{perl_sitearch}/PDL/Graphics/VRML*

#
# Demos
#
%dir %{perl_sitearch}/PDL/Demos
%{perl_sitearch}/PDL/Demos/BAD_*
%{perl_sitearch}/PDL/Demos/G*
%{perl_sitearch}/PDL/Demos/m51.fits

%dir %{perl_sitearch}/auto/PDL
%dir %{perl_sitearch}/auto/PDL/Graphics/

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
%attr(-,root,root) %{perl_sitearch}/auto/PDL/IO
%attr(-,root,root) %{perl_sitearch}/auto/PDL/ImageND
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Math
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Primitive
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Tests

%files perldl
%attr(755,root,root) %{_bindir}/perldl
%{_mandir}/man1/perldl*
%{perl_sitearch}/PDL/perldl*
%{perl_sitearch}/PDL/Demos/Screen*

%files Graphics-TriD
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Graphics/TriD
%dir %{perl_sitearch}/PDL/Graphics/TriD
%{perl_sitearch}/PDL/Graphics/TriD/[A-SU-Z]*
%{perl_sitearch}/PDL/Graphics/TriD/Te*
%{perl_sitearch}/PDL/Demos/TriD*

%files Graphics-TriD-Tk
%{perl_sitearch}/PDL/Graphics/TriD/Tk.pm
%{perl_sitearch}/PDL/Demos/TkTriD*

%files Graphics-PGPLOT
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Graphics/PGPLOT
%{perl_sitearch}/PDL/Graphics/PGPLOT*
%{perl_sitearch}/PDL/Graphics2D*
%{perl_sitearch}/PDL/Demos/PGPLOT*
%{perl_sitearch}/PDL/Demos/BAD2_*

%files Graphics-IIS
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Graphics/IIS
%{perl_sitearch}/PDL/Graphics/IIS*

%files Graphics-OpenGL
%attr(-,root,root) %{perl_sitearch}/auto/PDL/Graphics/OpenGL*
%{perl_sitearch}/PDL/Graphics/OpenGL*
