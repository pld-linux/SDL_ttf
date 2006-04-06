Summary:	Simple DirectMedia Layer - ttf handling
Summary(pl):	Biblioteka obs³ugi fontów TTF
Summary(pt_BR):	Simple DirectMedia Layer - Biblioteca de fontes TrueType
Name:		SDL_ttf
Version:	2.0.7
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_ttf/release/%{name}-%{version}.tar.gz
# Source0-md5:	0f6ee1a502e6913a412aac353dc75bbc
Patch0:		%{name}-ft2build_h.patch
URL:		http://www.libsdl.org/projects/SDL_ttf/
BuildRequires:	SDL-devel >= 1.2.5-2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a sample library which allows you to use TrueType fonts in
your SDL applications. It comes with an example program "sdlfont"
which displays an example string for a given TrueType font file.

%description -l pl
Przyk³adowa biblioteka do obs³ugi fontów TrueType w aplikacjach SDL.
Pakiet zawiera przyk³adowy program "sdlfont", wy¶wietlaj±cy
przyk³adowy ci±g znaków zadanym fontem TrueType.

%description -l pt_BR
Esta é uma biblioteca que permite a utilização de fontes TrueType em
suas aplicações SDL. Ela vem com o programa exemplo "showfont" que
mostra uma string exemplo para uma fonte TrueType fornecida.

%package devel
Summary:	Header files and more to develop SDL_ttf applications
Summary(pl):	Pliki nag³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_ttf
Summary(pt_BR):	Cabeçalhos para desenvolver programas utilizando a %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel

%description devel
Header files and more to develop SDL_ttf applications.

%description devel -l pl
Pliki nag³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_ttf.

%description devel -l pt_BR
Este pacote contém os cabeçalhos que programadores vão precisar para
desenvolver aplicações utilizando a %{name}.

%package static
Summary:	Static SDL_ttf libraries
Summary(pl):	Biblioteki statyczne SDL_ttf
Summary(pt_BR):	Biblioteca estática para desenvolvimento utilizando a %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SDL_ttf libraries.

%description static -l pl
Biblioteki statyczne SDL_ttf.

%description static -l pt_BR
Este pacote contém a biblioteca estática que programadores vão
precisar para desenvolver aplicações linkados estaticamente com a
%{name}.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install showfont $RPM_BUILD_ROOT%{_bindir}/sdlfont

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/SDL/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
