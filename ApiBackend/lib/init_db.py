# -*- coding: utf-8 -*-
__author__ = 'Hipeace86'
__date__ = '15-09-02'

if __name__ == "__main__":
    from Flavors.Entity.FlavorsModel import Flavors
    from Images.Entity.ImagesModel import Images
    from Instances.Entity.InstancesModel import Instances
    from Instances.Entity.InstanceSnapModel import InstanceSnap
    from Physical.Entity.PhysicalModel import Physical
    from Projects.Entity.ProjectsModel import Projects
    from Projects.Entity.ProjectUserModel import ProjectUser
    from Users.Entity.UsersModel import Users
    from Volumes.Entity.VolumesModel import Volumes
    from Volumes.Entity.VolumeSnapModel import VolumeSnap
    from Route import engine

    Flavors.__table__.create(engine, checkfirst=True)
    Images.__table__.create(engine, checkfirst=True)
    Instances.__table__.create(engine, checkfirst=True)
    InstanceSnap.__table__.create(engine, checkfirst=True)
    Physical.__table__.create(engine, checkfirst=True)
    Projects.__table__.create(engine, checkfirst=True)
    ProjectUser.__table__.create(engine, checkfirst=True)
    Users.__table__.create(engine, checkfirst=True)
    Volumes.__table__.create(engine, checkfirst=True)
    VolumeSnap.__table__.create(engine, checkfirst=True)
