Name:           ros-jade-rail-pick-and-place-msgs
Version:        1.1.5
Release:        0%{?dist}
Summary:        ROS rail_pick_and_place_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rail_pick_and_place_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib-msgs
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-message-runtime
Requires:       ros-jade-rail-manipulation-msgs
Requires:       ros-jade-sensor-msgs
BuildRequires:  ros-jade-actionlib-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-rail-manipulation-msgs
BuildRequires:  ros-jade-sensor-msgs

%description
Messages and Services for RAIL Pick and Place

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon May 04 2015 David Kent <davidkent@wpi.edu> - 1.1.5-0
- Autogenerated by Bloom

