%global tl_name latexcourse-rug
%global tl_revision 39026

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	A LaTeX course book
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latexcourse-rug
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcourse-rug.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcourse-rug.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the book and practice files for a LaTeX course that
the author has give several times at the Rijksuniversiteit Groningen
(Netherlands).

