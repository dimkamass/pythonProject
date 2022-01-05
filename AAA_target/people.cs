using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
namespace My_First_data
{
    #region People
    public class People
    {
        #region Member Variables
        protected int _id;
        protected string _name;
        protected string _bio;
        protected unknown _birthday;
        #endregion
        #region Constructors
        public People() { }
        public People(string name, string bio, unknown birthday)
        {
            this._name=name;
            this._bio=bio;
            this._birthday=birthday;
        }
        #endregion
        #region Public Properties
        public virtual int Id
        {
            get {return _id;}
            set {_id=value;}
        }
        public virtual string Name
        {
            get {return _name;}
            set {_name=value;}
        }
        public virtual string Bio
        {
            get {return _bio;}
            set {_bio=value;}
        }
        public virtual unknown Birthday
        {
            get {return _birthday;}
            set {_birthday=value;}
        }
        #endregion
    }
    #endregion
}