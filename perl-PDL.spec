%include	/usr/lib/rpm/macros.perl
%define		__find_provides	%{_builddir}/PDL-%{version}/find-perl-provides
%define		__find_requires %{_builddir}/PDL-%{version}/find-perl-requires
Summary:	perlDL
Summary(pl):	perlDL
Name:		perl-PDL
Version:	2.003
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.digital.com/pub/plan/perl/CPAN/modules/by-module/PDL/PDL-%{version}.tar.gz
Patch0:		perl-PDL-conf.patch
Patch1:		perl-PDL-dep.patch
URL:		http://www.perl.com/CPAN//modules/by-module/PDL/PDL-%{version}.readme
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	perl-Tk
BuildRequires:	perl-PGPLOT
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The perlDL project aims to turn perl into an efficient numerical language for
scientific computing. The PDL module gives standard perl the ability to
COMPACTLY store and SPEEDILY manipulate the large N-dimensional data sets which
are the bread and butter of scientific computing. e.g. C<$a=$b+$c> can add two
2048x2048 images in only a fraction of a second.

%description -l pl
perlDL rozsze¿a mo¿liwo¶ci perl'a o funkcje do obliczeñ numerycznych 
i naukowaych.

%prep
%setup  -q -n PDL-%{version}
%patch0 -p1 
%patch1 -p1

chmod +x find-*

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS -I/usr/include/ncurses -DNCURSES -DPERL_POLLUTE" 

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{perl_sitearch}/auto/PDL -name \*.so -exec \
	strip --strip-unneeded {} \;

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/PDL
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man{1,3}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[13]/*

%{perl_sitearch}/PDL
%{perl_sitearch}/PDL.pm
%dir %{perl_sitearch}/auto/PDL
%attr(-,root,root) %{perl_sitearch}/auto/PDL/*
