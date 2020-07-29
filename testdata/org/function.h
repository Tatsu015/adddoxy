#ifndef GTGFUNCTION_H
#define GTGFUNCTION_H

#include <QString>

class Test;

struct Struct1{
  int data_;
};

class Function {
public:
  enum Modifier : int32_t {
    Public,
    Protected,
    Private,
    Unknown,
  };

  struct Struct2 {
    int data_;
  };

public:
  Function();
  ~Function();

  QString getName() const;
  void setName(const QString& name);

  Modifier getModifier() const;
  void setModifier(const Modifier modifier);

  int func(int a, int b);

private:
  QString name_;
  Modifier modifier_;
};

#endif // GTGFUNCTION_H
