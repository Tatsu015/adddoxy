/**
 * @file function.h
 *
 * @brief @todo
 */
#ifndef GTGFUNCTION_H
#define GTGFUNCTION_H

#include <QString>

class Test;


/**
 * @brief Struct1は@todoの構造体
 *
 * @todo
 */
struct Struct1{
  /// @todo
  int data_;
};


/**
 * @brief Functionは@todoのクラス
 *
 * @todo
 */
class Function {
public:
  /**
  * @brief Modifierは@todoを示す列挙型
  *
  * @todo
  */
 enum Modifier : int32_t {
    Public,
    Protected,
    Private,
    Unknown,
  };


  /**
   * @brief Struct2は@todoの構造体
   *
   * @todo
   */
  struct Struct2 {
    /// @todo
    int data_;
  };

public:
  /**
   * @brief コンストラクタ
   *
   * @todo
   */
  Function();

  /**
   * @brief デストラクタ
   *
   * @todo
   */
  ~Function();


  /**
   * @brief nameのgetter
   *
   * \a nameを取得する。
   * \sa setName()
   */
  QString getName() const;

  /**
   * @brief nameのsetter
   *
   * \a nameを設定する。
   * \sa getName()
   */
  void setName(const QString& name);


  /**
   * @brief modifierのgetter
   *
   * \a modifierを取得する。
   * \sa setModifier()
   */
  Modifier getModifier() const;

  /**
   * @brief modifierのsetter
   *
   * \a modifierを設定する。
   * \sa getModifier()
   */
  void setModifier(const Modifier modifier);


  /**
   * @brief @todo
   *
   * @todo \a a  \a b
   */
  int func(int a, int b);

private:
  /// @todo
  QString name_;

  /// @todo
  Modifier modifier_;
};

#endif // GTGFUNCTION_H
