# If any of the following macros should be set otherwise,
# you can wrap any of them with the following conditions:
# - %%if 0%%{centos} == 7
# - %%if 0%%{?rhel} == 7
# - %%if 0%%{?fedora} == 23
# Or just test for particular distribution:
# - %%if 0%%{centos}
# - %%if 0%%{?rhel}
# - %%if 0%%{?fedora}
#
# Be aware, on centos, both %%rhel and %%centos are set. If you want to test
# rhel specific macros, you can use %%if 0%%{?rhel} && 0%%{?centos} == 0 condition.
# (Don't forget to replace double percentage symbol with single one in order to apply a condition)

# Generate devel rpm
%global with_devel 1
# Build project from bundled dependencies
%global with_bundled 0
# Build with debug info rpm
%global with_debug 0
# Run tests in check section
%global with_check 1
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif


%global provider        github
%global provider_tld    com
%global project         golang
%global repo            image
# https://github.com/golang/image
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          426cfd8eeb6e08ab1932954e09e3c2cb2bc6e36d
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20170514

# Following the model of golang-googlecode-text.spec to provide the x path
%global x_provider      golang
%global x_provider_tld  org
%global x_repo          image
%global x_import_path   %{x_provider}.%{x_provider_tld}/x/%{x_repo}
%global x_name          golang-%{x_provider}%{x_provider_tld}-%{repo}
%global devel_main      %{x_name}-devel

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.3.%{commitdate}.git%{shortcommit}%{?dist}
Summary:        Go supplementary image libraries
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}



%description
%{summary}

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(golang.org/x/text/encoding/charmap)
%endif

Requires:      golang(golang.org/x/text/encoding/charmap)

Provides:      golang(%{import_path}/bmp) = %{version}-%{release}
Provides:      golang(%{import_path}/colornames) = %{version}-%{release}
Provides:      golang(%{import_path}/draw) = %{version}-%{release}
Provides:      golang(%{import_path}/font) = %{version}-%{release}
Provides:      golang(%{import_path}/font/basicfont) = %{version}-%{release}
Provides:      golang(%{import_path}/font/gofont/gobold) = %{version}-%{release}
Provides:      golang(%{import_path}/font/gofont/gobolditalic) = %{version}-%{release}
Provides:      golang(%{import_path}/font/gofont/goitalic) = %{version}-%{release}
Provides:      golang(%{import_path}/font/gofont/gomedium) = %{version}-%{release}
Provides:      golang(%{import_path}/font/gofont/gomediumitalic) = %{version}-%{release}
Provides:      golang(%{import_path}/font/gofont/gomono) = %{version}-%{release}
Provides:      golang(%{import_path}/font/gofont/gomonobold) = %{version}-%{release}
Provides:      golang(%{import_path}/font/gofont/gomonobolditalic) = %{version}-%{release}
Provides:      golang(%{import_path}/font/gofont/gomonoitalic) = %{version}-%{release}
Provides:      golang(%{import_path}/font/gofont/goregular) = %{version}-%{release}
Provides:      golang(%{import_path}/font/gofont/gosmallcaps) = %{version}-%{release}
Provides:      golang(%{import_path}/font/gofont/gosmallcapsitalic) = %{version}-%{release}
Provides:      golang(%{import_path}/font/inconsolata) = %{version}-%{release}
Provides:      golang(%{import_path}/font/plan9font) = %{version}-%{release}
Provides:      golang(%{import_path}/font/sfnt) = %{version}-%{release}
Provides:      golang(%{import_path}/math/f32) = %{version}-%{release}
Provides:      golang(%{import_path}/math/f64) = %{version}-%{release}
Provides:      golang(%{import_path}/math/fixed) = %{version}-%{release}
Provides:      golang(%{import_path}/riff) = %{version}-%{release}
Provides:      golang(%{import_path}/tiff) = %{version}-%{release}
Provides:      golang(%{import_path}/tiff/lzw) = %{version}-%{release}
Provides:      golang(%{import_path}/vector) = %{version}-%{release}
Provides:      golang(%{import_path}/vp8) = %{version}-%{release}
Provides:      golang(%{import_path}/vp8l) = %{version}-%{release}
Provides:      golang(%{import_path}/webp) = %{version}-%{release}
Provides:      golang(%{import_path}/webp/nycbcra) = %{version}-%{release}

%package -n %{x_name}-devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(golang.org/x/text/encoding/charmap)
%endif

Requires:      golang(golang.org/x/text/encoding/charmap)

Provides:      golang(%{x_import_path}/bmp) = %{version}-%{release}
Provides:      golang(%{x_import_path}/colornames) = %{version}-%{release}
Provides:      golang(%{x_import_path}/draw) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/basicfont) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/gofont/gobold) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/gofont/gobolditalic) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/gofont/goitalic) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/gofont/gomedium) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/gofont/gomediumitalic) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/gofont/gomono) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/gofont/gomonobold) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/gofont/gomonobolditalic) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/gofont/gomonoitalic) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/gofont/goregular) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/gofont/gosmallcaps) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/gofont/gosmallcapsitalic) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/inconsolata) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/plan9font) = %{version}-%{release}
Provides:      golang(%{x_import_path}/font/sfnt) = %{version}-%{release}
Provides:      golang(%{x_import_path}/math/f32) = %{version}-%{release}
Provides:      golang(%{x_import_path}/math/f64) = %{version}-%{release}
Provides:      golang(%{x_import_path}/math/fixed) = %{version}-%{release}
Provides:      golang(%{x_import_path}/riff) = %{version}-%{release}
Provides:      golang(%{x_import_path}/tiff) = %{version}-%{release}
Provides:      golang(%{x_import_path}/tiff/lzw) = %{version}-%{release}
Provides:      golang(%{x_import_path}/vector) = %{version}-%{release}
Provides:      golang(%{x_import_path}/vp8) = %{version}-%{release}
Provides:      golang(%{x_import_path}/vp8l) = %{version}-%{release}
Provides:      golang(%{x_import_path}/webp) = %{version}-%{release}
Provides:      golang(%{x_import_path}/webp/nycbcra) = %{version}-%{release}


%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%description -n %{x_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{x_import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary:         Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{x_name}-devel = %{version}-%{release}

%if 0%{?with_check} && ! 0%{?with_bundled}
%endif

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

%build
%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
echo "%%dir %%{gopath}/src/%%{x_import_path}/." >> x_devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{x_import_path}/$file
    echo "%%{gopath}/src/%%{x_import_path}/$file" >> x_devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        echo "%%dir %%{gopath}/src/%%{x_import_path}/$dirprefix" >> x_devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/
# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{x_import_path}/$file
    echo "%%{gopath}/src/%%{x_import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{x_import_path}/$dirprefix" >> x_devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
# Include test data in unit tests subpackage
install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/testdata
install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/font/testdata
cp -rpav testdata %{buildroot}/%{gopath}/src/%{x_import_path}
cp -rpav font/testdata %{buildroot}/%{gopath}/src/%{x_import_path}/font
echo "%%{gopath}/src/%%{x_import_path}/testdata" >> unit-test-devel.file-list
echo "%%{gopath}/src/%%{x_import_path}/font/testdata" >> unit-test-devel.file-list
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
sort -u -o x_devel.file-list x_devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
# No dependency directories so far

export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{x_import_path}/bmp
%gotest %{x_import_path}/colornames
%gotest %{x_import_path}/draw
%gotest %{x_import_path}/font
%gotest %{x_import_path}/font/plan9font
%gotest %{x_import_path}/font/sfnt
%gotest %{x_import_path}/math/fixed
%gotest %{x_import_path}/riff
%gotest %{x_import_path}/tiff
# There are some precision problems with some architectures
# https://github.com/golang/go/issues/21460
# For now, We are skipping the failing tests for those arches
%ifnarch ppc64le s390x
%gotest %{x_import_path}/vector
%endif
%gotest %{x_import_path}/webp
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README CONTRIBUTING.md AUTHORS CONTRIBUTORS PATENTS
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}

%files -n %{x_name}-devel -f x_devel.file-list
%license LICENSE
%doc README CONTRIBUTING.md AUTHORS CONTRIBUTORS PATENTS
%dir %{gopath}/src/%{x_provider}.%{x_provider_tld}/x
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc README CONTRIBUTING.md AUTHORS CONTRIBUTORS PATENTS
%endif

%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20170514.git426cfd8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 15 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0-0.2.20170514.git426cfd8
- Do not run vector tests in ppcle and s390x due to precision issues

* Mon Aug 07 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0-0.1.20170514.git426cfd8
- First package for Fedora

